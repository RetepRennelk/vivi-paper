#FILE_BASE = lazaro2017
#DIR_BASE  = raptor/lazaro2017

FILE_BASE = {{FILE_BASE}}
DIR_BASE  = {{DIR_BASE}}

PDF = ./pdf/$(DIR_BASE).pdf
# Look actively for the ini-file, only if present it will be part of the prereqs
INI = $(wildcard ./pdf/$(DIR_BASE).ini)

SPLIT_PDF_DIR = ./build/split_pdf/$(DIR_BASE)
SPLIT_PDF     = $(SPLIT_PDF_DIR)/$(FILE_BASE).pdf

RST_DIR       = ./build/rst/$(DIR_BASE)
PNG_DIR       = $(RST_DIR)/png
RST_FILE      = $(RST_DIR)/$(FILE_BASE).rst

SPLIT_PNGS = $(shell python .\util\get_string_list_of_split_pngs.py $(PDF) $(INI))
DIRED_SPLIT_PNGS := $(addprefix $(PNG_DIR)/, $(SPLIT_PNGS))

all: ensure_dirs_exist clean_png_dir $(DIRED_SPLIT_PNGS) $(RST_FILE) 

ensure_dirs_exist:
	$(shell python util\ensure_dir_exists.py $(SPLIT_PDF_DIR))
	$(shell python util\ensure_dir_exists.py $(PNG_DIR))

# Delete extraneous pngs which may occur when changing the split factor	
clean_png_dir:
	$(shell python .\util\clean_png_dir.py $(PNG_DIR) $(SPLIT_PNGS))

$(PNG_DIR)/%.png: $(SPLIT_PDF)	
	$(eval pngnr := $(subst png,,$*))
	mutool convert -F png -O resolution=300 -o $@ $(SPLIT_PDF) $(pngnr)
	$(eval oldfilename := $(subst /,\,$(PNG_DIR)/$*1.png))
	$(eval newfilename := $(subst /,\,$(PNG_DIR)/$*.png))
	move /Y "$(oldfilename)" "$(newfilename)"
	
$(SPLIT_PDF): $(PDF) $(INI)
	$(shell python .\util\pdf_to_split_pdf.py $(SPLIT_PDF) $(PDF) $(INI))

$(RST_FILE): $(DIRED_SPLIT_PNGS)
	$(shell python .\util\make_rst.py $(RST_FILE) $(SPLIT_PNGS))
	
print_variables:
	$(info PNG_DIR = $(PNG_DIR))
	$(info DIRED_SPLIT_PNGS = $(DIRED_SPLIT_PNGS))
	$(info SPLIT_PNGS = $(SPLIT_PNGS))
	$(info SPLIT_PDF = $(SPLIT_PDF))
	
$(INI): ; @: