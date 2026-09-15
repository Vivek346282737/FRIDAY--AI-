from ai.brain import brain


response = '''

{
    "message": "Opening Chrome and searching OpenAI.",

    "actions": [

        {

            "action": "OPEN",

            "target": "chrome"

        },

        {

            "action": "BROWSER",

            "target": "search OpenAI"

        }

    ]

}

'''


result = brain.parse_response(

    response

)


print(

    result

)
