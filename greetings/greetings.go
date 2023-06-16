package greetings

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}
	message := fmt.Sprintf(randFormat(), name)
	return message, nil
}
func Love(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}
	var message string
	message = fmt.Sprintf("%v, I love you!", name)
	return message, nil
}
func Hellos(names []string) (map[string]string, error) {
	messages := make(map[string]string)
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		messages[name] = message
	}
	return messages, nil
}
func init() { //init()函数在程序启动时自动调用
	rand.Seed(time.Now().UnixMicro())
}
func randFormat() string {
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hali, %v! Well meet!",
	}
	return formats[rand.Intn(len(formats))]
}
