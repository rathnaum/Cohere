import cohere
from cohere.responses.classify import Example
co = cohere.Client('bVO9dbxD9nRoKBtE5PEvwJacOmKdFWrqYcrsRVR9') # This is your trial API key
response = co.classify(
  model='embed-english-v2.0',
  inputs=["my bill failed"],
  examples=[Example("I have a billing problem", "billing"), Example("My PC is not working", "system"), Example("order failed", "order"), Example("not able to place order", "order"), Example("system is very slow", "system"), Example("refund ", "billing")])
print('The confidence levels of the labels are: {}'.format(response.classifications))
