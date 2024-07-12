
(cl:in-package :asdf)

(defsystem "srv_func_package-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "add_int" :depends-on ("_package_add_int"))
    (:file "_package_add_int" :depends-on ("_package"))
  ))