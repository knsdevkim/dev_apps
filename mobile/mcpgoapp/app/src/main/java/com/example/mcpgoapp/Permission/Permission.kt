package com.example.mcpgoapp.Permission

import android.app.Activity
import android.content.pm.PackageManager
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

class Permission(val context: Activity) {
     fun initializePermissions() {
         this.generatePermissions()
     }

     private fun generatePermissions() {
        when (PackageManager.PERMISSION_GRANTED) {
            ContextCompat.checkSelfPermission(
                    context,
                    android.Manifest.permission.ACCESS_FINE_LOCATION
            ) -> {
                // GRANTED
            }
            ContextCompat.checkSelfPermission(
                    context,
                    android.Manifest.permission.ACCESS_COARSE_LOCATION
            ) -> {
                // GRANTED
            }
            ContextCompat.checkSelfPermission(
                context,
                android.Manifest.permission.CALL_PHONE
            ) -> {
                // GRANTED
            }
            else -> {
                ActivityCompat.requestPermissions(
                        context,
                        arrayOf(
                                android.Manifest.permission.ACCESS_FINE_LOCATION,
                                android.Manifest.permission.ACCESS_COARSE_LOCATION,
                                android.Manifest.permission.CALL_PHONE
                        ),
                        PERMISSIONS_CODE
                )
            }
        }
    }

    companion object {
        private val PERMISSIONS_CODE: Int = 1000
    }
}