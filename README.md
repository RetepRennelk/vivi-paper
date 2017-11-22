# vivi-paper

This set of tools is aimed to enable reflection on Research Papers after note-taking. It takes the notes taken and place them next to the page from where they were lifted.

The background is that for the most part reading a paper is forgetting a paper. This project is an 
attempt to put an end to running on this particular hamster wheel. The process comprises splitting pdfs in halves, transform them to images, and add comments next to them to create an annotated HTML view on the paper.

Development was done on Windows. So there are many idiosyncracies, which will prevent these tools to run on Linux - as is. If need be, one can implement the concept on Linux.

List of software dependencies, which must be accessible from anywhere on the command-line:
- GNU Make 3.81
- mutools
- pandoc

## Process

Start of with a pdf which may have two columns.

![Source PDF](./img/source_pdf.png)

The command `make.py build` splits the pdf in halve per default. It is possible to not split the pdf in halves. The resulting first pages look as below.

![First split PDF](./img/split_pdf1.png)

![Second split PDF](./img/split_pdf2.png)

In addition an rst-file is created looking like this:

![Restructured File](./img/restruct_init.png)

*IMPORTANT NOTE*: Copy the pre-built restuctured file from `build/rst `to the `./rst`-folder. This is in order to be able to edit freely.

From here on the command `make.py html` translates the rst-file in the `./rst`-folder and as a final result an HTML-file is generated.

![Final HTML](./img/final_html.png)
