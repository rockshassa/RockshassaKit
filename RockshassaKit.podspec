#
# Be sure to run `pod lib lint RockshassaKit.podspec' to ensure this is a
# valid spec and remove all comments before submitting the spec.
#
# Any lines starting with a # are optional, but encouraged
#
# To learn more about a Podspec see http://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = "RockshassaKit"
  s.version          = "0.1.0"
  s.summary          = "A collection of utility scripts that do work on your Xcode project."
  s.description      = <<-DESC
                       A magical collection of utility scripts that do work on your Xcode project
                       DESC
  s.homepage         = "https://bitbucket.org/rockshassa/rockshassakit.git"
  # s.screenshots     = "www.example.com/screenshots_1", "www.example.com/screenshots_2"
  s.license          = 'MIT'
  s.author           = { "Nicholas Galasso" => "nick@rockshassa.com" }
  s.source           = { :git => "https://bitbucket.org/rockshassa/rockshassakit.git", :tag => s.version.to_s }
  # s.social_media_url = 'https://twitter.com/<TWITTER_USERNAME>'

  s.platform     = :ios, '8.0'
  s.requires_arc = true

  s.source_files = 'Pod/Classes/**/*'
  s.resource_bundles = {
    'RockshassaKit' => ['Pod/Assets/*.png']
  }

  # s.public_header_files = 'Pod/Classes/**/*.h'
  # s.frameworks = 'UIKit', 'MapKit'
  # s.dependency 'AFNetworking', '~> 2.3'
end
