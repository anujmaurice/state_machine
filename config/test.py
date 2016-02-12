

RM_PROCESS = {
	"start": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","rsyslog","start"],
			"verify":"sudo service rsyslog status |grep -q running"
	},
	"stop": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","rsyslog","stop"],
			"verify":"sudo service rsyslog status |grep -q stopped"
	}
}
