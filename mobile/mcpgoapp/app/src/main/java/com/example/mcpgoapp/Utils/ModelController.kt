package com.example.mcpgoapp.Utils

import android.content.Context
import io.realm.Realm
import io.realm.RealmConfiguration

class ModelController {

    fun modelInitialize(context: Context) {
        Realm.init(context)
        val config = RealmConfiguration.Builder()
                .name("mcpgo.realm")
                .schemaVersion(1)
                .allowWritesOnUiThread(true)
                .build()
        Realm.setDefaultConfiguration(config)
    }

    fun modelInstance(): Realm {
        return Realm.getDefaultInstance()
    }
}