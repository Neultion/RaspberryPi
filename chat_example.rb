require 'rubygems'
require 'mqtt'
require 'readline'
#nickname
nickname = ARGV[0]

#localhost test
mqtt = MQTT::Client.new('localhost')

mqtt.connect do |client|
    client.subscribe('chat/public')
    client.subscribe("chat/private/#{nickname}")
    enter_msg = "#{nickname} enter room!!"
    client.publish 'chat/public', enter_msg

    #Publish Thread
    Thread.new do
        while message = Readline.readline("", true)
            case message
            when /^\/priv\s*(\w*)\s*(.*)/   #individual message
                client.publish "chat/private/#{$1}","<#{nickname}> : #{$2}"
            when /^\/quit\s*(.*)/  #exit
                client.publish 'chat/public' , "#{nickname} has quit (#{$1})"
                exit 1
            else
                client.publish 'chat/public' , "#{nickname} : #{message}"
            end
        end
    end
    # Nhận và in tin nhắn
    client.get do |topic, msg|
        puts "\n[#{topic}] #{msg}"
        print "[#{nickname}] > \n"
    end
end
