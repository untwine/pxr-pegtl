import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import copy


class PxrPegtlConan(ConanFile):
    name = "pxr-pegtl"
    version = "26.8"
    package_type = "header-library"
    license = "LicenseRef-TOST-1.0"
    homepage = "https://github.com/untwine/pxr-pegtl"
    url = "https://github.com/untwine/pxr-pegtl"
    description = "Parsing Expression Grammar library used in OpenUSD"
    topics = ("pixar", "open-usd")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "cmake/*", "src/*", "LICENSE.txt", "NOTICE.txt"

    def layout(self):
        cmake_layout(self)

    def package_id(self):
        self.info.clear()

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE.txt", self.source_folder,
             os.path.join(self.package_folder, "licenses"))
        copy(self, "NOTICE.txt", self.source_folder,
             os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.set_property("system_package_version", "0.26.8")
        self.cpp_info.builddirs = ["share/cmake/pxr-pegtl"]
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
