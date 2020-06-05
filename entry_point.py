config = {
    "see-you-in-thirty-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 30.0,
        "args": ('hello11',)
    },
    "see-you-in-ten-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 10.0,
        "args": ('hello22',)
    }
}
