import Foundation
import JavaScriptKit

func sendSwitchLampOnRequest(storm: LedStorm) {
  let url = "/lamp"
  let body = composeBodyFromLedStorm(storm)
  let fetchPromise: JSPromise = fetch(url, body)
  fetchPromise.then { _ -> String in
    print("Lamp turned on!")
    return ""
  } failure: { error -> String in
    print("Error turning lamp on \(error)")
    return ""
  }
}

func sendLightningRequest(storm: LedStorm) {
  let url = "/lightning"
  let body = composeBodyFromLedStorm(storm)
  let fetchPromise: JSPromise = fetch(url, body)
  fetchPromise.then { _ -> String in
    print("Lightning triggered!")
    return ""
  } failure: { error -> String in
    print("Error sending lightning \(error)")
    return ""
  }
}

private func fetch(_ url: String, _ body: JSValue) -> JSPromise {
  let _jsFetch = JSObject.global.fetch.function!
  let headers = JSObject.global
  headers["Content-Type"] = "application/json"
  let requestData = JSObject.global
  requestData["method"] = "POST"
  requestData["headers"] = ["Content-Type": "application/json"].jsValue()
  requestData["body"] = body
  print(requestData)
  return JSPromise(_jsFetch(url, requestData).object!)!
}

typealias RequestBody = [String: ConvertibleToJSValue]

private func composeBodyFromLedStorm(_ storm: LedStorm) -> JSValue {
  """
  {
      "lightnings": [
          {
              "r": \(storm.lightning1.color.red),
              "g": \(storm.lightning1.color.green),
              "b": \(storm.lightning1.color.blue)
          },
          {
              "r": \(storm.lightning2.color.red),
              "g": \(storm.lightning2.color.green),
              "b": \(storm.lightning2.color.blue)
          }
      ]
  }
  """.jsValue()
}
