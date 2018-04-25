from __future__ import print_function
import json
from watson_developer_cloud import ConversationV1

class DictQuery(dict):
    def get(self, path, default = None):
        keys = path.split("/")
        val = None
        
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [ v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)
            
            if not val:
                break;
        return val

conversation = ConversationV1(
    username='57db025b-2f83-45b6-90e9-4890d0d3e616',
    password='COcz1TPoSKQD',
    version='2018-04-25')
workspace_id = '2c730ca5-72d1-44d0-a1d9-a12327957f18'
def main():
    text = ''
    response = ''
    while text != 'quit':
        text = raw_input('>> ')
        response = conversation.message(
                                    workspace_id=workspace_id, input={
                                    'text': text
                                    })
        data = json.dumps(response)
        print(", ".join(DictQuery(response).get('intents/intent')))

if __name__ == "__main__":
    main()

