import Foundation
import TokamakDOM

struct LightningColorPicker: View {
  let lightningNumber: Int
  let selectedColor: LightningColor
  let onColorSelected: (LightningColor) -> ()
  var body: some View {
    VStack {
      HStack {
        Spacer().frame(width: 16)
        ForEach(colors, id: \.self) { color in
          VStack {
            Button(action: {
              onColorSelected(color)
            }, label: {
              // Hack needed to be able to show the colors.
              // A butto can't render a Pixel view inside, it has to be a text :(
              Text("_")
            }).buttonStyle(PixelButtonStyle(color: color.asSwiftUIColor()))
          }
        }
        Spacer().frame(width: 16)
      }
      Spacer().frame(height: 10)
      HStack {
        Text("Lightning # \(lightningNumber)")
        Spacer().frame(width: 20)
        Pixel(color: selectedColor).frame(height: 20).frame(width: 20).cornerRadius(10.0)
      }
    }
  }
}

struct Pixel: View {
  let color: LightningColor
  var body: some View {
    color.asSwiftUIColor()
  }
}

private extension LightningColor {
  func asSwiftUIColor() -> Color {
    Color(
      red: Double(red) / 255,
      green: Double(green) / 255,
      blue: Double(blue) / 255,
      opacity: 1.0
    )
  }
}

private let colors: [LightningColor] = {
  let colorStep = 50
  let upRange = stride(from: 0, to: 255, by: colorStep)
  let downRange = stride(from: 255, to: 0, by: colorStep * -1)
  var colors: [LightningColor] = []
  // Reds
  upRange.forEach { color in
    let color = LightningColor(red: 255, green: color, blue: 0)
    colors.append(color)
  }
  // Yellows
  downRange.forEach { color in
    let color = LightningColor(red: color, green: 255, blue: 0)
    colors.append(color)
  }
  // Greens
  upRange.forEach { color in
    let color = LightningColor(red: 0, green: 255, blue: color)
    colors.append(color)
  }
  // Blues
  downRange.forEach { color in
    let color = LightningColor(red: 0, green: color, blue: 255)
    colors.append(color)
  }
  // Purples
  upRange.forEach { color in
    let color = LightningColor(red: color, green: 0, blue: 255)
    colors.append(color)
  }
  // Pinks
  downRange.forEach { color in
    let color = LightningColor(red: 255, green: 0, blue: color)
    colors.append(color)
  }
  return colors
}()
