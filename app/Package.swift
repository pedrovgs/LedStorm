// swift-tools-version:5.3
import PackageDescription
let package = Package(
    name: "app",
    platforms: [.macOS(.v11)],
    products: [
        .executable(name: "app", targets: ["app"]),
    ],
    dependencies: [
        .package(name: "Tokamak", url: "https://github.com/TokamakUI/Tokamak", from: "0.7.0"),
    ],
    targets: [
        .target(
            name: "app",
            dependencies: [
                .product(name: "TokamakShim", package: "Tokamak"),
            ]
        ),
        .testTarget(
            name: "appTests",
            dependencies: ["app"]
        ),
    ]
)
