import TokamakDOM

struct LightningColorPicker: View {
  let lightningNumber: Int
  var body: some View {
    VStack {
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
      Spacer().frame(height: 10)
      Text("Lightning # \(lightningNumber)")
    }
  }
}

struct Pixel: View {
  let color: Color
  var body: some View {
    color
  }
}

private var colors: [Color] {
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
