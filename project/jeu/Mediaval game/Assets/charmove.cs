using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterMotor : MonoBehaviour {
	Animation animations;

	public float walkspeed;
	public float runspeed;
	public float turnspeed;
	// input
	public string inputFront;
	public string inputBack;
	public string inputLeft;
	public string inputRight;

	public Vector3 jumpspeed;
	CapsuleCollider playerCollider;

	void Start () {
		animation = GameObject.GetComponent<Animation>();
		playerCollider = GameObject.GetComponent<CapsuleCollider>();

		
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetKey(inputFront))
		{
			transform.Translate(0,0,walkspeed * Time.deltaTime);
			animations.Play("walk");
		}
		if(Input.GetKey(inputBack))
		{
			transform.Translate(0,0,-(walkspeed/2) * Time.deltaTime);
			animations.Play("walk");
		}
		if(Input.GetKey(inputLeft))
		{
			transform.Rotate(0,-turnspeed * Time.deltaTime,0);
	
		}
		if(Input.GetKey(inputRight))
		{
			transform.Rotate(0,turnspeed * Time.deltaTime,0);

		}
		
	}
}
