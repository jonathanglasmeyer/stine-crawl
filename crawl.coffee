Nightmare = require 'nightmare'
fs = require 'fs'

$ = require 'jquery'

args = process.argv.slice(2)
username = args[0]
password = args[1]

crawl = ->
  new Nightmare()
    .goto('https://www.stine.uni-hamburg.de')
    .wait '#logIn_btn'
    .type 'input#field_user', username
    .type 'input#field_pass', password
    .click '#logIn_btn'
    .wait()
    .click '.link000267'
    .wait()
    .click '.link000364'
    .wait()
    .evaluate (
      (page) -> $('table#tbMonth.nb').html()),
      (res) -> console.log res
    .run (err, nightmare) ->
      if (err) then console.log '' else console.log ''


crawl()



