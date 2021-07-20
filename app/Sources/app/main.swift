import TokamakDOM

struct LedStormApp: App {
  var body: some Scene {
    WindowGroup("Tokamak App") {
      LedStormView()
    }
  }
}

struct LedStormView: View {
  @State private var count: Int = 0
  var body: some View {
    VStack {
      Spacer()
      Button(
        action: {
          print("CLICK")
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

extension Color {
  static let buttonPressed = Color(red: 1.0, green: 1.0, blue: 1.0, opacity: 1.0)
}

LedStormApp.main()
