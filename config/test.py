

RM_PROCESS = {
	"start": {
			"hostname":"desktop",
			"user":"amaurice",
            "name":"rsyslog",
			"command":["sudo","service","rsyslog","start"],
			"verify":"sudo service rsyslog status |grep -q running"
	},
	"stop": {
			"hostname":"desktop",
			"user":"amaurice",
            "name":"rsyslog",
			"command":["sudo","service","rsyslog","stop"],
			"verify":"sudo service rsyslog status |grep -q stopped"
	}
}

HTTPD_PROCESS = {
	"start": {
			"hostname":"desktop",
			"user":"amaurice",
            "name":"httpd",
			"command":["sudo","service","httpd","start"],
			"verify":"sudo service httpd status |grep -q running"
	},
	"stop": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","httpd","stop"],
			"verify":"sudo service httpd status |grep -q stopped"
	}
}
ZNC_PROCESS = {
	"start": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","znc","start"],
			"verify":"sudo service znc status |grep -q running"
	},
	"stop": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","znc","stop"],
			"verify":"sudo service znc status |grep -q stopped"
	}
}

POSTFIX_PROCESS = {
	"start": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","postfix","start"],
			"verify":"sudo service postfix status |grep -q running"
	},
	"stop": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":["sudo","service","postfix","stop"],
			"verify":"sudo service postfix status |grep -q stopped"
	}
}

COMMAND_1 = {
	"yeah": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":"""
            ps -aux |wc -l;
            echo $?;
            pwd;
            """,
			"verify":"ls -l;"
	},
	"oh": {
			"hostname":"desktop",
			"user":"amaurice",
			"command":"""
            w;
            uptime;
            hostname;""",
			"verify":"date"
	}
}
