package com.example.stihealthtrackingapp.Fragments

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.TextView
import androidx.fragment.app.Fragment
import com.android.volley.Request
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.bumptech.glide.Glide
import com.example.stihealthtrackingapp.R
import com.example.stihealthtrackingapp.Urls.Https
import org.json.JSONObject
import java.util.*

class ProfileFragment: Fragment() {

    private lateinit var mProfile: ImageView
    private lateinit var mFullname: TextView
    private lateinit var mAddress: TextView
    private lateinit var mGender: TextView
    private lateinit var mBirthdate: TextView
    private lateinit var mMobile: TextView
    private lateinit var mEmail: TextView
    private lateinit var mQrcode: ImageView
    private lateinit var mProgress: ProgressBar

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val fragmentView: View = inflater.inflate(R.layout.fragment_profile, container, false)

        this.setupWidgets(fragmentView)

        this.fetchAPIData()

        return fragmentView
    }
    
    companion object {
        private const val TAG = "ProfileFragment"
    }

    private fun setupWidgets(v: View) {
        mProfile = v.findViewById(R.id.profile)
        mFullname = v.findViewById(R.id.fullname)
        mAddress = v.findViewById(R.id.address)
        mGender = v.findViewById(R.id.gender)
        mBirthdate = v.findViewById(R.id.birthdate)
        mMobile = v.findViewById(R.id.mobile)
        mEmail = v.findViewById(R.id.email)
        mQrcode = v.findViewById(R.id.qrcode)
        mProgress = v.findViewById(R.id.progress)

        this.initializeWidgets()
    }

    private fun initializeWidgets() {
        mProgress.visibility = View.INVISIBLE
    }

    private fun fetchAPIData() {
        mProgress.visibility = View.VISIBLE

        try {
            val queue = Volley.newRequestQueue(activity!!)

            val sharedPref = activity!!.getSharedPreferences("app", Context.MODE_PRIVATE)

            val request = StringRequest(
                Request.Method.GET,
                "${Https().HTTPS_GETPROFILEINFO}?id=${sharedPref.getString("id", "")}",
                { response ->
                    try {

                        mProgress.visibility = View.INVISIBLE

                        val jsonObject = JSONObject(response)
                        val jsonArray = jsonObject.getJSONArray("data")

                        for (i in 0 until jsonArray.length()) {
                            val dataObject = jsonArray.getJSONObject(i)

                            Glide.with(activity!!)
                                .load("${Https().IP}/${dataObject.getString("proofimage")}")
                                .error(R.drawable.ic_user_black_foreground)
                                .into(mProfile)

                            Glide.with(activity!!)
                                .load("${Https().IP}/${dataObject.getString("qrcode")}")
                                .error(R.drawable.ic_qrcode_black_foreground)
                                .into(mQrcode)

                            mFullname.text = dataObject.getString("fullname").toUpperCase(Locale.ROOT)
                            mAddress.text = dataObject.getString("address").toUpperCase(Locale.ROOT)
                            mGender.text = dataObject.getString("sex").toUpperCase(Locale.ROOT)
                            mBirthdate.text = dataObject.getString("birthdate")
                            mMobile.text = dataObject.getString("mobile")
                            mEmail.text = dataObject.getString("email")
                        }
                    } catch(e: Exception) {
                        mProgress.visibility = View.INVISIBLE

                        e.message?.let { message ->
                            Log.e(TAG, message)
                        }
                    }
                }, { error ->
                    mProgress.visibility = View.INVISIBLE

                    error.message?.let { message ->
                        Log.e(TAG, message)
                    }
                })

            queue.add(request)
        } catch(e: Exception) {
            mProgress.visibility = View.INVISIBLE

            e.message?.let { message ->
                Log.e(TAG, message)
            }
        }
    }
}