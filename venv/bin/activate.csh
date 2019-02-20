# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.
# Created by Davide Di Blasi <davidedb@gmail.com>.

<<<<<<< HEAD
alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; test "\!:*" != "nondestructive" && unalias deactivate && unalias pydoc'
=======
set newline='\
'

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH:q" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT:q" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; test "\!:*" != "nondestructive" && unalias deactivate && unalias pydoc'
>>>>>>> a18dfbc216f4bffdff9bcaa5344ec31f407952ea

# Unset irrelevant variables.
deactivate nondestructive

<<<<<<< HEAD
setenv VIRTUAL_ENV "/Users/Fer/Desktop/RevocBank/venv"

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"
=======
setenv VIRTUAL_ENV "/home/fern/Desktop/RevocBank/venv"

set _OLD_VIRTUAL_PATH="$PATH:q"
setenv PATH "$VIRTUAL_ENV:q/bin:$PATH:q"
>>>>>>> a18dfbc216f4bffdff9bcaa5344ec31f407952ea



if ("" != "") then
    set env_name = ""
else
<<<<<<< HEAD
    set env_name = `basename "$VIRTUAL_ENV"`
=======
    set env_name = "$VIRTUAL_ENV:t:q"
>>>>>>> a18dfbc216f4bffdff9bcaa5344ec31f407952ea
endif

# Could be in a non-interactive environment,
# in which case, $prompt is undefined and we wouldn't
# care about the prompt anyway.
if ( $?prompt ) then
<<<<<<< HEAD
    set _OLD_VIRTUAL_PROMPT="$prompt"
    set prompt = "[$env_name] $prompt"
=======
    set _OLD_VIRTUAL_PROMPT="$prompt:q"
if ( "$prompt:q" =~ *"$newline:q"* ) then
    :
else
    set prompt = "[$env_name:q] $prompt:q"
endif
>>>>>>> a18dfbc216f4bffdff9bcaa5344ec31f407952ea
endif

unset env_name

alias pydoc python -m pydoc

rehash
<<<<<<< HEAD

=======
>>>>>>> a18dfbc216f4bffdff9bcaa5344ec31f407952ea
