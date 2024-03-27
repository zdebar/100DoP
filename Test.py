obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
 
def collectString(d):
    collection = []
    for value in d.values():
        if isinstance(value, dict):
            collection += collectString(value)
        elif isinstance(value, str):
            collection.append(value)
    return collection


print(collectString(obj))

