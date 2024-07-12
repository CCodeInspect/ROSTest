;; Auto-generated. Do not edit!


(when (boundp 'srv_func_package::AddInts)
  (if (not (find-package "SRV_FUNC_PACKAGE"))
    (make-package "SRV_FUNC_PACKAGE"))
  (shadow 'AddInts (find-package "SRV_FUNC_PACKAGE")))
(unless (find-package "SRV_FUNC_PACKAGE::ADDINTS")
  (make-package "SRV_FUNC_PACKAGE::ADDINTS"))
(unless (find-package "SRV_FUNC_PACKAGE::ADDINTSREQUEST")
  (make-package "SRV_FUNC_PACKAGE::ADDINTSREQUEST"))
(unless (find-package "SRV_FUNC_PACKAGE::ADDINTSRESPONSE")
  (make-package "SRV_FUNC_PACKAGE::ADDINTSRESPONSE"))

(in-package "ROS")





(defclass srv_func_package::AddIntsRequest
  :super ros::object
  :slots (_num1 _num2 ))

(defmethod srv_func_package::AddIntsRequest
  (:init
   (&key
    ((:num1 __num1) 0)
    ((:num2 __num2) 0)
    )
   (send-super :init)
   (setq _num1 (round __num1))
   (setq _num2 (round __num2))
   self)
  (:num1
   (&optional __num1)
   (if __num1 (setq _num1 __num1)) _num1)
  (:num2
   (&optional __num2)
   (if __num2 (setq _num2 __num2)) _num2)
  (:serialization-length
   ()
   (+
    ;; int32 _num1
    4
    ;; int32 _num2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _num1
       (write-long _num1 s)
     ;; int32 _num2
       (write-long _num2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _num1
     (setq _num1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num2
     (setq _num2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass srv_func_package::AddIntsResponse
  :super ros::object
  :slots (_sum ))

(defmethod srv_func_package::AddIntsResponse
  (:init
   (&key
    ((:sum __sum) 0)
    )
   (send-super :init)
   (setq _sum (round __sum))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:serialization-length
   ()
   (+
    ;; int32 _sum
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sum
       (write-long _sum s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sum
     (setq _sum (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass srv_func_package::AddInts
  :super ros::object
  :slots ())

(setf (get srv_func_package::AddInts :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get srv_func_package::AddInts :datatype-) "srv_func_package/AddInts")
(setf (get srv_func_package::AddInts :request) srv_func_package::AddIntsRequest)
(setf (get srv_func_package::AddInts :response) srv_func_package::AddIntsResponse)

(defmethod srv_func_package::AddIntsRequest
  (:response () (instance srv_func_package::AddIntsResponse :init)))

(setf (get srv_func_package::AddIntsRequest :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get srv_func_package::AddIntsRequest :datatype-) "srv_func_package/AddIntsRequest")
(setf (get srv_func_package::AddIntsRequest :definition-)
      "int32 num1
int32 num2
---
int32 sum
")

(setf (get srv_func_package::AddIntsResponse :md5sum-) "4781436a0c2affec8025955a6041e481")
(setf (get srv_func_package::AddIntsResponse :datatype-) "srv_func_package/AddIntsResponse")
(setf (get srv_func_package::AddIntsResponse :definition-)
      "int32 num1
int32 num2
---
int32 sum
")



(provide :srv_func_package/AddInts "4781436a0c2affec8025955a6041e481")


