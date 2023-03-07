from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
import platform
import psutil

from app.db.db import get_db

router = APIRouter()


@router.get('/', include_in_schema=False)
@router.get('')
async def health(db: AsyncIOMotorClient = Depends(get_db)):
    try:
        # Check if the database is responsive
        await db.command('ping')
        db_status = 'up'
    except Exception:
        db_status = 'down'

    # Get system information
    system_info = {
        "system": platform.system(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict()
    }

    return {
        "database": db_status,
        "system_info": system_info
    }
