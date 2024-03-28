# Demo on how to set up OpenAI

This project utilizes:

| Type      | Tech                                                                                                     |
| --------- | -------------------------------------------------------------------------------------------------------- |
| Language  | [Python](https://www.python.org/)                                                                        |
| Framework | [FastAPI](https://fastapi.tiangolo.com/)                                                                 |
| Hosting   | [AWS](https://aws.amazon.com/) (Lambda + API Gateway)                                                    |
| Other     | [OpenAI](https://openai.com/), [AWS CDK](https://aws.amazon.com/cdk/), [Docker](https://www.docker.com/) |

# To Run

1. Clone the repository.
2. Get and set your OpenAI API Key to local env. [OpenAIKey]{https://platform.openai.com/api-keys}
3. Install FastAPI and OpenAI using pip. CDK/Docker is not required for testing.
4. In the terminal, navigate to the `src` folder.
5. Run `python brandforge.py -i "herbal tea"`.

You will see some output such as:

```
User input: herbal tea
Generate upbeat branding snippet for herbal tea:
Snippet: "Awaken your senses with our refreshing herbal teas! Sip on nature's goodness and feel energized and rejuvenated with every cup. Embrace the power...
Generate related branding keywords for herbal tea:
Result: ['natural', 'organic', 'relaxation', 'wellness', 'purify', 'herbal remedy', 'plant', 'based']
```

**Note:** A UI should be implemented to demonstrate the actual functionality.

## Helpful Commands

```bash
pip install fastapi
pip install openai
pip install uvicorn
```
