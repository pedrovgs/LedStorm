import Foundation
import JavaScriptKit
import TokamakDOM
import TokamakShim

struct LedStormApp: App {
  var body: some Scene {
    WindowGroup("Tokamak App") {
      LedStormView()
    }
  }
}

var colors: [Color] {
  let colorStep = 50
  let upRange = stride(from: 0, to: 255, by: colorStep)
  let downRange = stride(from: 255, to: 0, by: colorStep * -1)
  var colors: [Color] = []
  // Reds
  upRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: 1.0, green: rangeColor, blue: 0, opacity: 1.0)
    colors.append(color)
  }
  // Yellows
  downRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: rangeColor, green: 1.0, blue: 0, opacity: 1.0)
    colors.append(color)
  }
  // Greens
  upRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: 0, green: 1.0, blue: rangeColor, opacity: 1.0)
    colors.append(color)
  }
  // Blues
  downRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: 0, green: rangeColor, blue: 1.0, opacity: 1.0)
    colors.append(color)
  }
  // Purples
  upRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: rangeColor, green: 0, blue: 1.0, opacity: 1.0)
    colors.append(color)
  }
  // Pinks
  downRange.forEach { color in
    let rangeColor = Double(color) / 255
    let color = Color(red: 1, green: 0, blue: rangeColor, opacity: 1.0)
    colors.append(color)
  }
  return colors
}

struct ColorPicker: View {
  var body: some View {
    HStack {
      ForEach(colors, id: \.self) { color in
        VStack {
          Button(action: {
            print("Tapped on color \(color)")
          }, label: {
            Text("_")
          }).buttonStyle(PixelButtonStyle(color: color))
        }
      }
    }
  }
}

struct Pixel: View {
  let color: Color
  var body: some View {
    color
  }
}

struct LedStormView: View {
  @State private var count: Int = 0
  var body: some View {
    VStack {
      ColorPicker()
      Spacer()
      Button(
        action: {
          sendLightningRequest()
        },
        label: {
          Text("⚡️").font(.system(size: 160))
        }
      ).buttonStyle(TransparentButtonStyle())
    }
  }
}

struct TransparentButtonStyle: ButtonStyle {
  func makeBody(configuration: Configuration) -> some View {
    let isPressed = configuration.isPressed
    return configuration
      .label.background(isPressed ? Color.buttonPressed : Color.clear)
  }
}

struct PixelButtonStyle: ButtonStyle {
  let color: Color
  func makeBody(configuration: Configuration) -> some View {
    configuration
      .label.background(color).frame(width: 10).frame(height: 10)
  }
}

extension Color {
  static let buttonPressed = Color(red: 0.29, green: 0.29, blue: 0.29, opacity: 1.0)
}

LedStormApp.main()

private func sendLightningRequest() {
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

func fetch(_ url: String, _ body: RequestBody) -> JSPromise {
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
