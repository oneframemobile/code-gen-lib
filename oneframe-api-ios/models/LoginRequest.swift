//
// LoginRequest.swift
//
// Generated by oneframemobile
// https://github.com/oneframemobile/networking-swagger-swift
//

import Networking
import Foundation


public class LoginRequest: Serializable {
    
    public var email: String
    public var password: String
    
    public init(email: String, password: String) {
        self.email = email
        self.password = password
    }
}
