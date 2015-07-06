Pod::Spec.new do |s|
  s.name             = "RockshassaKit"
  s.version          = "0.1.0"
  s.summary          = "A collection of utility scripts that do work on your Xcode project."
  s.description      = <<-DESC
                       A magical collection of utility scripts that do work on your Xcode project
                       DESC
  s.homepage         = "https://github.com/rockshassa/RockshassaKit.git"
  s.license          = 'MIT'
  s.author           = { "Nicholas Galasso" => "nick@rockshassa.com" }
  s.source           = { :git => "https://github.com/rockshassa/RockshassaKit.git", :tag => s.version.to_s }
  s.social_media_url = 'http://rockshassa.com'

  s.platform     = :ios, '8.0'
  s.requires_arc = true

  s.source_files = 'Pod/**/*'
  s.resource_bundles = {
    'RockshassaKit' => ['Pod/Assets/*.png']
  }
end
