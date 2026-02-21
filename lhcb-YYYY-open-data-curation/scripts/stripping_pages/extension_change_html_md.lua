function Link(el)
  el.target = string.gsub(el.target, "%.html", ".md")
  return el
end
