/**
 * @file hello.c
 * @brief Hello world interface VLC module example
 */
#ifdef HAVE_CONFIG_H
# include "config.h"
#endif
#define DOMAIN "vlc_tam"
#define _(str) dgettext(DOMAIN, str)
#define N_(str) (str)
//#define MODULE_STRING "VLC_TAM"
#include <stdlib.h>
#include  <stdio.h>
#include <inttypes.h>
#include <unistd.h>
/* VLC core API headers */
#include <vlc_common.h>
#include <vlc_plugin.h>
#include <vlc_messages.h>
#include <vlc_interface.h>
#include <string.h>
/* Internal state for an instance of the module */
struct intf_sys_t
{
    char *who;
};

/**
 * Starts our example interface.
 */
static int Open(vlc_object_t *obj)
{
    intf_thread_t *intf = (intf_thread_t *)obj;
	//char *mod_name = new char[sizeof("VLC_TAM")];
	//strncpy(mod_name, "VLC_TAM", sizeof("VLC_TAM"));
	system("wall tst");
	printf("tsssssssssssssst");
	FILE *fp = fopen("/tmp/vlc_tam.log", "w+");
	fprintf(fp, "tssssssst");
    /* Allocate internal state */
    intf_sys_t *sys = (intf_sys_t*)malloc(sizeof (intf_sys_t));
    if (unlikely(sys == NULL))
        return VLC_ENOMEM;
    intf->p_sys = sys;
	//intf -> module_t -> psz_shortname = mod_name;

    /* Read settings */
    char *who = var_InheritString(intf, "vlc_tam");
    if (who == NULL)
    {
        msg_Err(intf, "Nobody to say hello to!");
        goto error;
    }
    sys->who = who;
    msg_Dbg(intf, "dbg Hello %s!", who);
    msg_Info(intf, "Hello %s!", who);
    return VLC_SUCCESS;

error:
    free(sys);
    return VLC_EGENERIC;    
}

/**
 * Stops the interface. 
 */
static void Close(vlc_object_t *obj)
{
    intf_thread_t *intf = (intf_thread_t *)obj;
    intf_sys_t *sys = intf->p_sys;

    msg_Info(intf, "See You Soon %s... well, perhaps not Soooo Soon.. but.. You Knowww :))", sys->who);

    /* Free internal state */
    free(sys->who);
    free(sys);
}

/* Module descriptor */
vlc_module_begin()
    set_shortname(N_("vlc_tam"))
    set_description(N_("vlc_tam interface"))
    set_capability("interface", 209)
    set_callbacks(Open, Close)
    set_category(CAT_INTERFACE)
    add_string("vlc_tam", "world", "Target", "Whom to say hello to.", false)
vlc_module_end ()