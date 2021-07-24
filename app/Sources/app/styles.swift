import TokamakDOM

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

private extension Color {
  static let buttonPressed = Color(red: 0.29, green: 0.29, blue: 0.29, opacity: 1.0)
}
