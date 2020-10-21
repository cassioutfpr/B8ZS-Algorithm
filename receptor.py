import socket
import matplotlib.pyplot as plt

def bin_to_string(msg):
	msg_out = ""
	msg_aux1 = ""
	msg_aux2 = msg
	for j in range(int(len(msg)/8)):
		msg_aux1 = msg_aux2[:8]
		msg_aux2 = msg_aux2[8:]
		msg_8_bits = msg_aux1[0] + msg_aux1[1] + msg_aux1[2] + msg_aux1[3] + msg_aux1[4] + msg_aux1[5] + msg_aux1[6] + msg_aux1[7]
		#print("msg 8 bits: " + msg_8_bits)
		an_integer = int(msg_8_bits, 2)
		ascii_character = chr(an_integer)
		msg_out += ascii_character

	return msg_out

def remove_minus(msg):
	vetor = []
	n_pass = True
	for j in range(len(msg)):
		if n_pass == True:
			if msg[j] != "-":
				vetor.append(int(msg[j]))
			else:
				vetor.append(2)
				n_pass = False
		else:
			n_pass = True

	return vetor

def array_to_binary(vetor):
	vetor_out = []
	for elem in vetor:
		if elem == 1:
			vetor_out.append(1)
		elif elem == 2:
			vetor_out.append(1)
		else:
			vetor_out.append(0)
	return vetor_out

def print_B8ZS_client(msg):
	vetor_in = remove_minus(msg)
	vetor = []
	vetor2 = []
	indexes_zeros = []
	i = 0
	k = 1
	number_of_zeros = 0
	last_non_zero = 0

	for elem in vetor_in:
		if i > 0 and i + 8 <= len(vetor_in) - 1:
			if vetor_in[i-1] == 1:
				if(vetor_in[i] == 0 and vetor_in[i+1] == 0 and vetor_in[i+2] == 0 and vetor_in[i+3] == 1 and vetor_in[i+4] == 2 and vetor_in[i+5] == 0 and vetor_in[i+6] == 2 and vetor_in[i+7] == 1):
					indexes_zeros.append(i)

		if vetor_in[i-1] == 2:
			if(vetor_in[i] == 0 and vetor_in[i+1] == 0 and vetor_in[i+2] == 0 and vetor_in[i+3] == 2 and vetor_in[i+4] == 1 and vetor_in[i+5] == 0 and vetor_in[i+6] == 1 and vetor_in[i+7] == 2):
				indexes_zeros.append(i)
	
		i = i + 1

		for elem2 in indexes_zeros:
			vetor_in[elem2] = 0
			vetor_in[elem2+1] = 0
			vetor_in[elem2+2] = 0
			vetor_in[elem2+3] = 0
			vetor_in[elem2+4] = 0
			vetor_in[elem2+5] = 0
			vetor_in[elem2+6] = 0
			vetor_in[elem2+7] = 0

	for elem in vetor_in:
		if elem == 1:
			vetor.append(1)
			last_non_zero = 1
		elif elem == 2:
			vetor.append(-1)
		else:
			vetor.append(0)

		vetor2.append(k)
		k = k + 1

	#print(vetor2)
	#print(vetor)
	plt.stem(vetor2,vetor)
	plt.show()

	vetor = array_to_binary(vetor_in)

	msg_ret = ""
	for elem in vetor:
		msg_ret += str(elem)

	print("Mensagem decodificada B8ZS: " + msg_ret)
	return msg_ret


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1234))
s.connect(('34.95.206.69', 3389))

msg = s.recv(1024)
msg = msg.decode("utf-16")
#msg = "000-1101-11-11-11-11-11-1"
print("Mensagem recebida: " + msg)

msg_to_string = print_B8ZS_client(msg)
msg_to_string = bin_to_string(msg_to_string)
print("Mensagem decodificada total: " + msg_to_string)



#an_integer = int(msg, 2)
#ascii_character = chr(an_integer)
#print(ascii_character)
#print(hex(ord(ascii_character)))
