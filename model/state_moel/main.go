package main

import (
	"fmt"
	"time"
)

func NewSimpleTrafficLight(speedLimit int) *TrafficLight {
	return &TrafficLight{
		SpeedLimit: speedLimit,
		State:      NewRedState(),
	}
}

type TrafficLight struct {
	State      LightState
	SpeedLimit int
}

func (tl *TrafficLight) TransitionState(newState LightState) {
	tl.State = newState
	tl.State.EnterState()
}

type LightState interface {
	Light()
	EnterState()
	NextLight(light *TrafficLight)
	CarPassingSpeed(*TrafficLight, int, string)
}

type DefaultLightState struct {
	StateName string
}

func (state *DefaultLightState) CarPassingSpeed(road *TrafficLight, speed int, licensePlate string) {
	if speed > road.SpeedLimit {
		fmt.Printf("Car with license %s was speeding\n", licensePlate)
	}
}
func (state *DefaultLightState) EnterState() {
	fmt.Printf("change state to: %s\n", state.StateName)
}

type redState struct {
	*DefaultLightState
}

func NewRedState() *redState {
	state := &redState{&DefaultLightState{StateName: "RED"}}
	return state
}
func (state *redState) Light() {
	fmt.Println("红灯亮起，不可行驶")
}
func (state *redState) CarPassingSpeed(light *TrafficLight, speed int, licensePlate string) {
	if speed > 0 {
		fmt.Printf("Car with license %s ran a red light!\n", licensePlate)
	}
}
func (state *redState) NextLight(light *TrafficLight) {
	light.TransitionState(NewGreenState())
}

type greenState struct {
	*DefaultLightState
}

func NewGreenState() *greenState {
	state := &greenState{&DefaultLightState{StateName: "GREEN"}}
	return state
}
func (state *greenState) Light() {
	fmt.Println("绿灯亮起，请行驶")
}
func (state *greenState) NextLight(light *TrafficLight) {
	light.TransitionState(NewAmberState())
}

type amberState struct {
	*DefaultLightState
}

func NewAmberState() *amberState {
	state := &amberState{&DefaultLightState{StateName: "AMBER"}}
	return state
}
func (state *amberState) Light() {
	fmt.Println("黄灯亮起，请注意")
}
func (state *amberState) NextLight(light *TrafficLight) {
	light.TransitionState(NewRedState())
}

func main() {
	trafficLight := NewSimpleTrafficLight(500)

	interval := time.NewTicker(5 * time.Second)

	for {
		select {
		case <-interval.C:
			trafficLight.State.Light()
			trafficLight.State.CarPassingSpeed(trafficLight, 25, "苏U99999")
			trafficLight.State.NextLight(trafficLight)
		default:
		}
	}
}
