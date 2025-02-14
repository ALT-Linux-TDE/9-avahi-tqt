prefix=@prefix@
exec_prefix=${prefix}
libdir=@libdir@
includedir=@includedir@

Name: avahi-tqt
Description: Avahi Multicast DNS Responder (TQT Support)
Version: @PACKAGE_VERSION@
Libs: -L${libdir} -lavahi-tqt
Cflags: -D_REENTRANT -I${includedir}
