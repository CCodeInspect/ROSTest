
(cl:in-package :asdf)

(defsystem "func_package-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "person" :depends-on ("_package_person"))
    (:file "_package_person" :depends-on ("_package"))
  ))