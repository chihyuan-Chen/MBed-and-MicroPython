# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-src"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-build"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/tmp"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/src/greentea-client-populate-stamp"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/src"
  "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/src/greentea-client-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/src/greentea-client-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "E:/CoreMaker-01/cmake_build/AIOT2101/develop/GCC_ARM/_deps/greentea-client-subbuild/greentea-client-populate-prefix/src/greentea-client-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
