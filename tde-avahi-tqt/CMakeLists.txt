#################################################
#
#  (C) 2015 Slávek Banko
#  slavek (DOT) banko (AT) axis.cz
#
#  Improvements and feedback are welcome
#
#  This file is released under GPL >= 2
#
#################################################

include_directories(
  ${CMAKE_BINARY_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${TQT_INCLUDE_DIRS}
)

link_directories(
  ${TQT_LIBRARY_DIRS}
)


##### library ###################################

set( target avahi-tqt )

tde_add_library(
  ${target} SHARED
  VERSION 1.0.0
  SOURCES qt-watch.cpp
  LINK ${AVAHI_COMMON} ${TQT_LIBRARIES}
  DESTINATION ${LIB_INSTALL_DIR}
)

tde_add_library(
  ${target} STATIC_PIC
  SOURCES qt-watch.cpp
  LINK ${AVAHI_COMMON} ${TQT_LIBRARIES}
  DESTINATION ${LIB_INSTALL_DIR}
)

add_custom_command(
  OUTPUT
    qt-watch.moc3
  COMMAND
    ${MOC_TQT_SCRIPT}
    ${MOC_EXECUTABLE}
    ${CMAKE_CURRENT_SOURCE_DIR}/qt-watch.cpp
    qt-watch.moc3
)

set_property(
  SOURCE qt-watch.cpp
  APPEND PROPERTY OBJECT_DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/qt-watch.moc3
)


##### headers ###################################

install(
  FILES qt-watch.h
  DESTINATION ${INCLUDE_INSTALL_DIR}/${CMAKE_PROJECT_NAME}
)

