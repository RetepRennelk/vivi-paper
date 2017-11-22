#FILE_BASE = lazaro2017
#DIR_BASE  = raptor/lazaro2017

FILE_BASE = {{FILE_BASE}}
DIR_BASE  = {{DIR_BASE}}

HTML_DIR       = ./html/$(DIR_BASE)
HTML_FILE      = $(HTML_DIR)/$(FILE_BASE).html
RST_DIR        = ./rst/$(DIR_BASE)

PNG_SRC_DIR    = $(RST_DIR)/png
PNG_TARGET_DIR = $(HTML_DIR)/png

PATH_TO_STYLES_CSS = $(shell python util\get_path_to_style_css.py $(HTML_FILE))

command     = $(subst /,\,$(PNG_SRC_DIR)/*.png)
PNGS        = $(shell dir $(command) /b)
HTML_PNGS   := $(addprefix $(PNG_TARGET_DIR)/,$(PNGS))

all: ensure_dir_exist $(HTML_PNGS) $(HTML_FILE) 
	
ensure_dir_exist:
	$(shell python util\ensure_dir_exists.py $(PNG_TARGET_DIR))
	
$(HTML_DIR)/%.html: $(RST_DIR)/%.rst
	$(info @ $@)
	$(info < $<)
	pandoc -s -c $(PATH_TO_STYLES_CSS) -f rst "$<" -o "$@"
	
$(PNG_TARGET_DIR)/%.png: $(PNG_SRC_DIR)/%.png
	mklink /H $(subst /,\,"$@" "$<")

temp:
	$(info $(HTML_FILE))
	$(info $(PATH_TO_STYLES_CSS))
