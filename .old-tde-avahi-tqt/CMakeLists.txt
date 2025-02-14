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


##### set project version ########################

include( TDEVersion )
cmake_minimum_required( VERSION ${TDE_CMAKE_MINIMUM_VERSION} )
tde_set_project_version( )


##### general package setup #####################

project( avahi-tqt )
set( PACKAGE avahi-tqt )
set( PACKAGE_VERSION 0.6.30 )


##### include essential cmake modules ###########

include( CheckSymbolExists )
include( FindPkgConfig )


##### include our cmake modules #################

include( TDEMacros )


##### setup install paths #######################

include( TDESetupPaths )
tde_setup_paths( )


##### optional stuff

option( WITH_ALL_OPTIONS "Enable all optional support" OFF )
option( WITH_GCC_VISIBILITY "Enable fvisibility and fvisibility-inlines-hidden" ${WITH_ALL_OPTIONS} )


##### setup architecture flags ##################

tde_setup_architecture_flags( )

include(TestBigEndian)
test_big_endian(WORDS_BIGENDIAN)

tde_setup_largefiles( )


##### configure checks ##########################

find_package( TQt )
set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TQT_CXX_FLAGS}" )
set( MOC_TQT_SCRIPT "${TQT_PREFIX}/bin/moc-tqt" )
if( NOT EXISTS ${MOC_TQT_SCRIPT} )
  tde_message_fatal( "moc-tqt not found!\n Check tqt installation." )
endif( NOT EXISTS ${MOC_TQT_SCRIPT} )

message( STATUS "Checking for avahi-common library" )
find_library( AVAHI_COMMON NAMES avahi-common )
if( NOT AVAHI_COMMON )
  tde_message_fatal( "avahi-common library are required, but not found on your system" )
endif( )
message( STATUS "  found ${AVAHI_COMMON}" )

if( WITH_GCC_VISIBILITY )
  tde_setup_gcc_visibility( )
  add_definitions( -D__TDE_HAVE_GCC_VISIBILITY )
endif( )


#### pkg-config #################################

set( prefix ${CMAKE_INSTALL_PREFIX} )
string( REGEX REPLACE "^${CMAKE_INSTALL_PREFIX}" "\${prefix}"
        exec_prefix ${EXEC_INSTALL_PREFIX} )
string( REGEX REPLACE "^${EXEC_INSTALL_PREFIX}" "\${exec_prefix}"
        libdir ${LIB_INSTALL_DIR} )
string( REGEX REPLACE "^${CMAKE_INSTALL_PREFIX}" "\${prefix}"
        includedir ${INCLUDE_INSTALL_DIR} )

configure_file( ${CMAKE_PROJECT_NAME}.pc.cmake ${CMAKE_PROJECT_NAME}.pc @ONLY )
install( FILES ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}.pc
         DESTINATION ${PKGCONFIG_INSTALL_DIR} )


##### build #####################################

tde_auto_add_subdirectories()

