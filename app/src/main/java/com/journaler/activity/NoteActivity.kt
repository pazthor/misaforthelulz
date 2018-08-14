package com.journaler.activity

import com.journaler.R

class NoteActivity : ItemActivity() {
    override val tag = "Note.Activty"
    override fun getLayout() = R.layout.activity_note
    override fun getActivityTittle() = R.string.app_name

}
