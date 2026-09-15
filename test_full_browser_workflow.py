from ai.executor import executor


response = {

    "message": "Testing complete browser workflow.",

    "actions": [

        {
            "action": "BROWSER",
            "target": "start browser"
        },

        {
            "action": "BROWSER",
            "target": "open google.com"
        },

        {
            "action": "BROWSER",
            "target": "wait 2"
        },

        {
            "action": "BROWSER",
            "target": "search ChatGPT"
        },

        {
            "action": "BROWSER",
            "target": "wait 2"
        },

        {
            "action": "BROWSER",
            "target": "click ChatGPT"
        },

        {
            "action": "BROWSER",
            "target": "wait 3"
        },

        {
            "action": "BROWSER",
            "target": "scroll down"
        },

        {
            "action": "BROWSER",
            "target": "wait 2"
        },

        {
            "action": "BROWSER",
            "target": "back"
        },

        {
            "action": "BROWSER",
            "target": "wait 1"
        },

        {
            "action": "BROWSER",
            "target": "close browser"
        }

    ]
}


result = executor.execute(
    response
)


print()

print(
    "FINAL RESULT:"
)

print(
    result
)
