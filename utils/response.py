response_get_note={
        200: {
            "description": "Notes list successfully fetched",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "status": 200,
                        "data": [
                            {
                                "id": "abc123",
                                "title": "Shopping List",
                                "content": "Buy milk and eggs",
                                "user_id": "user123",
                                "created_at": "2025-09-14T10:00:00Z"
                            }
                        ]
                    }
                }
            },
        }
    }
response_set_note={
        200: {
            "description": "Notes list successfully fetched",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "status": 200,
                        "data": 
                            {
                                "id": "abc123",
                                "title": "Shopping List",
                                "content": "Buy milk and eggs",
                                "user_id": "user123",
                                "created_at": "2025-09-14T10:00:00Z"
                            }
                        
                    }
                }
            },
        }
    }
response_update_note={
        200: {
            "description": "Notes list successfully fetched",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "status": 200,
                        "data": [
                            {
                                "id": "abc123",
                                "title": "Shopping List",
                                "content": "Buy milk and eggs",
                            }
                        ]
                    }
                }
            },
        }
    }
response_delete_note={
        200: {
            "description": "Notes list successfully fetched",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "status": 200,
                         "message": "Note deleted"
                    }
                }
            },
        }
    }