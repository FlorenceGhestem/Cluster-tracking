source("renv/activate.R")
missing_pkgs <- names(which(!sapply(
  X = c("languageserver", "httpgd", "lintr", "styler", "gert", "prompt", "svglite", "ragg"),
  FUN = function(x) nzchar(system.file(package = x))
)))
if (length(missing_pkgs) > 0) {
  message(
    "Please install the missing packages using: `renv::install(c(",
    paste(sprintf('"%s"', missing_pkgs), collapse = ", "),
    "))`, then restart your R session!"
  )
}
rm(missing_pkgs)
