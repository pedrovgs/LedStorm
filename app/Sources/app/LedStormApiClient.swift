import JavaScriptKit

func sendLightningRequest() {
  print("CLICK")
  let url = "http://raspberrypi.local"
  let lightning1 = ["r": 255, "g": 255, "b": 255].jsValue()
  let lightning2 = ["r": 255, "g": 255, "b": 255].jsValue()
  let body: [String: ConvertibleToJSValue] = ["lightnings": [lightning1, lightning2]]
  let fetchPromise: JSPromise = fetch(url, body)
  fetchPromise.then { value -> String in
    print("Value = \(value)")
    return ""
  } failure: { error -> String in
    print("Error = \(error)")
    return ""
  }
}

private func fetch(_ url: String, _ body: RequestBody) -> JSPromise {
  let _jsFetch = JSObject.global.fetch.function!
  let headers = JSObject.global
  headers["Content-Type"] = "application/json"
  let requestData = JSObject.global
  requestData["method"] = "POST"
  requestData["headers"] = ["Content-Type": "application/json"].jsValue()
  requestData["body"] = """
  {
      "lightnings": [
          {
              "r": 255,
              "g": 255,
              "b": 255
          },
          {
              "r": 255,
              "g": 213,
              "b": 255
          }
      ]
  }
  """
  print(requestData)
  return JSPromise(_jsFetch(url, requestData).object!)!
}

typealias RequestBody = [String: ConvertibleToJSValue]
