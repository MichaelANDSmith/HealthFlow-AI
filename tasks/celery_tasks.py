from app import celery
from app.models.time_management import generate_daily_schedule
from app.utils import logger
from datetime import datetime
import time
from typing import Dict, Any
from celery.exceptions import MaxRetriesExceededError
from app.exceptions import ScheduleGenerationError

@celery.task(
    bind=True,
    max_retries=3,
    soft_time_limit=300,
    time_limit=330,
    autoretry_for=(ScheduleGenerationError,),
    retry_backoff=True,
    retry_jitter=True,
    retry_kwargs={'max_retries': 3}
)
def async_generate_schedule(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Asynchronous task to generate a personalized daily schedule with enhanced features.
    
    Features:
    - Automatic retries on failure
    - Progress tracking
    - Comprehensive logging
    - Timeout handling
    - Input validation
    
    Args:
        user_data: Dictionary containing user preferences and constraints including:
            - work_hours: List of available work hours
            - preferences: User scheduling preferences
            - tasks: List of tasks to schedule
            - timezone: User's timezone
    
    Returns:
        Dict: Generated schedule containing:
            - tasks: Scheduled tasks with time slots
            - metadata: Generation timestamp and stats
    
    Raises:
        ScheduleGenerationError: If schedule cannot be generated
        ValueError: If input data is invalid
    """
    # Validate input
    if not all(k in user_data for k in ['work_hours', 'preferences', 'tasks']):
        error_msg = "Invalid user_data: missing required fields"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    try:
        start_time = time.time()
        logger.info(f"Starting schedule generation for user {user_data.get('user_id', 'unknown')}")
        
        # Update task state (visible in monitoring tools)
        self.update_state(state='PROGRESS', meta={'progress': 10})
        
        # Simulate time-consuming processing (replace with actual work)
        time.sleep(2)  # Initial processing
        
        self.update_state(state='PROGRESS', meta={'progress': 50})
        
        # Generate the actual schedule
        schedule = generate_daily_schedule(user_data)
        
        self.update_state(state='PROGRESS', meta={'progress': 90})
        
        # Add metadata
        schedule['metadata'] = {
            'generated_at': datetime.utcnow().isoformat(),
            'processing_time': time.time() - start_time,
            'tasks_scheduled': len(schedule.get('tasks', [])),
            'user_id': user_data.get('user_id')
        }
        
        logger.info(
            f"Successfully generated schedule with {len(schedule.get('tasks', []))} tasks "
            f"in {time.time() - start_time:.2f} seconds"
        )
        
        return schedule
    
    except Exception as e:
        logger.error(f"Schedule generation failed: {str(e)}", exc_info=True)
        
        # Special handling for retryable errors
        if isinstance(e, ScheduleGenerationError) and self.request.retries < self.max_retries:
            logger.warning(f"Retrying schedule generation (attempt {self.request.retries + 1})")
            raise self.retry(exc=e)
        
        # Wrap non-specific errors
        if not isinstance(e, (ScheduleGenerationError, ValueError)):
            e = ScheduleGenerationError(f"Schedule generation failed: {str(e)}")
        
        raise e
