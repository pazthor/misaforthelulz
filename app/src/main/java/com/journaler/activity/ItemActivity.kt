package com.journaler.activity

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import com.journaler.R
import com.journaler.model.MODE
import java.sql.Savepoint

//open class ItemActivity : BaseActivity() {
//
//    override val tag = "Item.Activity"
//    override fun getLayout() = R.layout.activity_item
//    override fun getActivityTittle() = R.string.app_name
//
//
//
//}

abstract class ItemActivity : BaseActivity() {
    protected var mode = MODE.VIEW
    override fun getActivityTittle() = R.string.app_name
    override fun onCreate(saveInstanceState: Bundle?){
        super.onCreate(saveInstanceState)
        val modeToSet = intent.getIntExtra(MODE.EXTRAS_KEY,
                MODE.VIEW.mode)
        mode = MODE.getByValue(modeToSet)
        Log.v(tag, "mode [$mode]")
    }
}