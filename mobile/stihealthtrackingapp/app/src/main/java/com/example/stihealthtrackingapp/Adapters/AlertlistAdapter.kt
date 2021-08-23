package com.example.stihealthtrackingapp.Adapters

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.stihealthtrackingapp.DataHandlers.AlertlistHandler
import com.example.stihealthtrackingapp.R

class AlertlistAdapter(val mContext: Context, val mList: ArrayList<AlertlistHandler>): RecyclerView.Adapter<AlertlistAdapter.ViewHolder>() {
    class ViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val date = view.findViewById<TextView>(R.id.date)
        val level = view.findViewById<TextView>(R.id.level)
        val status = view.findViewById<TextView>(R.id.status)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view: View = LayoutInflater.from(mContext).inflate(R.layout.recycler_alertlist, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.date.text = this.mList[position].date
        holder.level.text = this.mList[position].level
        holder.status.text = this.mList[position].status
    }

    override fun getItemCount(): Int {
        return this.mList.size
    }
}