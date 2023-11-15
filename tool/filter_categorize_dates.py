from datetime import datetime
events = [
{ "name": "Hackathon: 2021",      
      "description": "Explore the exciting project submissions from the fall 2021 XRPL Hackathon that focused on the NFT and Hooks smart contract functionalities on the ledger.",
      "type": "hackathon",
      "link": "https://xrpl-hackathon-2021.devpost.com/project-gallery",
      "location": "Virtual",
      "date": "September 13-October 6, 2021",
      "image": "Hackathons.png",
      "end_date": "October 6, 2021",
      },
      
    { "name": "XRPL Community Meetup: San Diego",      
      "description": "The first official Meetup hosted by the XRPL Community. Community members in Southern California gathered around a firepit and shared their experiences with the XRPL.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrpl-community/events/281806645/",
      "location": "San Diego, CA",
      "date": "Saturday, November 20, 2021",
      "image": "event-meetup-san-diego@2x.jpg",
      "end_date": "November 20, 2021",
      },

    { "name": "XRPL Community Meetup: Atlanta",      
      "description": "The inaugural Meetup in the Southeast region of the United States got community members excited to meet like-minded individuals in their area.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrpl-community/events/281980446/",
      "location": "Atlanta, GA",
      "date": "Saturday, November 27, 2021",
      "image": "event-meetup-alanta@2x.jpg",
      "end_date": "November 27, 2021",
    },
    { "name": "XRPL Community Meetup: San Francisco",      
      "description": "Community members in the Bay Area with diverse backgrounds in technology and beyond met in downtown San Francisco.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrpl-community/events/281806676/",
      "location": "San Francisco, CA",
      "date": "Monday, November 29, 2021",
      "image": "event-meetup-san-francisco@2x.jpg",
      "end_date": "November 29, 2021",
      },

    { "name": "XRPL Community Meetup: Miami",      
      "description": "One of the biggest Meetups held so far, this was the first of an ongoing series of local XRPL Community Meetup events in Miami. ",
      "type": "meetup",
      "link": "https://www.meetup.com/xrpl-community/events/281829463/",
      "location": "Miami, FL ",
      "date": "Thursday, December 9, 2021",
      "image": "event-meetup-miami@2x.jpg",
      "end_date": "December 8, 2022",
      },

    { "name": "XRPL Community Meetup: Nashville",      
      "description": "Nashville-based members of the XRPL Community came together to network, learn, share ideas, and form new partnerships. ",
      "type": "meetup",
      "link": "https://www.meetup.com/xrp-ledger-nashville-community/events/282538189/",
      "location": "Nashville, TN",
      "date": "Saturday, December 18, 2021",
      "image": "event-meetup-nashville@2x.jpg",
      "end_date": "December 18, 2022",
      },
      

    { "name": "NYC Meetup/Hackathon XRPL Celebration",
      "id": "upcoming-xrpl-new-york",
      "description": "The NYC/XRP community and Dev Null Productions cordially invites you to attend our 10th meetup, being held in celebration of the on-going XRPL Hackathon, at the unique and artistic TALS studio in Midtown Manhattan.",
      "type": "meetup",
      "link": "https://www.meetup.com/NYC-XRP/events/284485901/",
      "location": "NYC, NY",
      "date": "March 30, 2022",
      "image": "event-meetup-new-york@2x.jpg",
      "end_date": "March 30, 2022",
      },
    
    { "name": "XRPL Community Meetup: London",
      "id": "upcoming-xrpl-london",
      "description": "Join for an evening of programming and networking with members of the XRPL Community in London, co-organised by Peerkat - the NFT platform for creators on the XRPL.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrp-ledger-london-community/events/283536458/",
      "location": "IDEALondon",
      "date": "March 31, 2022",
      "image": "event-meetup-london.png",
      "end_date": "March 31, 2022",
      },
      
    { "name": "XRPL Community Meetup: Toronto",
      "id": "upcoming-xrpl-toronto",
      "description": "Join us for our first Toronto meetup with an evening of programming and networking with other members of the XRP Ledger Community with special guests from the XUMM Wallet and ARK PLATES teams!",
      "type": "meetup",
      "link": "https://www.meetup.com/xrpl-toronto-community-meetup/events/284177188/",
      "location": "Toronto",
      "date": "March 31, 2022",
      "image": "event-meetup-toronto@2x.jpg",
      "end_date": "March 31, 2022",
      },
      
    { "name": "XRPL Community Meetup: San Diego",
      "id": "upcoming-xrpl-san-diego",
      "description": "Get together with other San Diego-based members of the XRP Ledger Community to network and discuss all things XRPL! Join us for our second San Diego XRPL Meetup.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrp-ledger-san-diego-community/events/284663355/",
      "location": "San Diego, CA",
      "date": "April 1st 2022",
      "image": "event-meetup-san-diego@2x.jpg",
      "end_date": "April 1, 2022",
      },

    { "name": "XRPL Community Meetup: Irvine LA",
      "id": "upcoming-xrpl-irvine",
      "description": "Get together with other LA-based members of the XRP Ledger Community to network and discuss all things XRPL.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrp-ledger-la-community-meetup/events/284824635/",
      "location": "UC Irvine, CA",
      "date": "April 3rd 2022",
      "image": "event-meetup-irvine@2x.jpg",
      "end_date": "April 2, 2022",
      },
      
    { "name": "XRPL Community Meetup: Miami #2",
      "id": "upcoming-xrpl-miami-2",
      "description": "We're excited to host our second Miami meetup for XRP Ledger community members on April 6th from 6-8pm, featuring Marco Neri, Developer Advocate at Ripple, who will join us to give a presentation on the XRP Ledger.",
      "type": "meetup",
      "link": "https://www.meetup.com/xrp-ledger-miami-community/events/284463736/",
      "location": "The LAB Miami, FL",
      "date": "April 6th 2022",
      "image": "event-meetup-miami@2x.jpg",
      "end_date": "April 6, 2022",
      },

    { "name": "Hackathon:<br />New Year, New NFT",
      "id": "upcoming-xrpl-hackathon-new-year",
      "description": "Build Functional NFTs that span across a full range of use cases.",
      "type": "hackathon",
      "link": "https://xrplnft2022.devpost.com/",
      "location": "Virtual",
      "date": "January 31 - March 14, 2022",
      "image": "Hackathons.png",
      "end_date": "March 14, 2022",
      },
      

    { "name": "Hackathon: Creating Real World Impact",      
      "description": "Build apps to improve lives in the real world using any of the SDKs and APIs for the XRP Ledger.",
      "type": "hackathon",
      "link": "https://xrplimpact.devpost.com/",
      "location": "Virtual",
      "date": "May 26 - Jul 11, 2022",
      "image": "Hackathons.png",
      "end_date" : "July 11, 2022",
      },

    { "name": "Conference:<br />Apex 2021",      
      "description": "View sessions from the Apex 2021 stages in Las Vegas and Tallinn.",
      "type": "conference",
      "link": "https://www.youtube.com/playlist?list=PLJQ55Tj1hIVZgnreb8ODgxJW032M9Z2XZ",
      "location": "Las Vegas, Tallinn",
      "date": "September 29-30, 2021",
      "image": "Conference.png",
      "end_date": "September 30, 2022",
      },

    { "name": "Hackathon:<br />NFT Launch Party",      
    "description": "Build Functional NFTs that span across a full range of use cases.",
    "type": "hackathon",
    "link": "https://xrplnft.devpost.com/",
    "location": "Virtual",
    "date": "Oct 31 - Dec 12, 2022",
    "image": "Hackathons.png",
    "end_date": "December 12, 2022",
    },
    { "name": "XRPL Zone @ Consensus",      
    "description": "XRPL Zone: your all-in-one location for creating and collaborating on XRP Ledger (XRPL) projects.",
    "type": "zone",
    "link": "https://xrplzone-consensus.splashthat.com/",
    "location": "Austin, Texas",
    "date": "April 27, 2023",
    "image": "XRPLZone.png",
    "end_date": "April 27, 2023"
    },
    { "name": "XRPL Developer AMAs",      
    "description": "A chat with Crossmark about wallet development on the XRP Ledger!",
    "type": "ama",
    "link": "https://discord.com/invite/xrpl",
    "location": "XRPL Developers Discord",
    "date": "April 14, 2023",
    "image": "AMAs.png",
    "end_date": "April 14, 2023"
    },
    { "name": "NFTs with xrp.cafe",      
    "description": "A cozy discussion with xrp.cafe about NFTs and the future of NFT infrastructure on the XRP Ledger.",
    "type": "ama",
    "link": "https://dev.to/ripplexdev/xrpcafe-ama-on-xrpl-developers-discord-36gp",
    "location": "XRPL Developers Discord",
    "date": "January 1, 2023",
    "image": "AMAs.png",
    "end_date": "January 1, 2023"
    },
    { "name": "Community Calls #1",      
    "description": "An open discussion about the development of XLS-20 and NFTs on the XRP Ledger.",
    "type": "cc",
    "link": "https://youtu.be/KpSt0PFT2QM",
    "location": "XRPL Developers Discord",
    "date": "June 02, 2022",
    "image": "CommunityCalls.png",
    "end_date": "June 02, 2022"
    },
    { "name": "Community Calls #2",      
    "description": "A community call about XRPL amendments with Chris McKay.",
    "type": "cc",
    "link": "https://youtu.be/oNJ1Qqns2Gw",
    "location": "XRPL Developers Discord",
    "date": "August 8, 2022",
    "image": "CommunityCalls.png",
    "end_date": "August 8, 2022"
    },
    { "name": "AMAs: POS and Crypto Payments with FriiPay",      
    "description": "A discussion with FriiPay about payment rails and POS integrations through the XRP Ledger",
    "type": "ama",
    "link": "https://dev.to/ripplexdev/xrpl-developer-ama-pos-and-crypto-payments-with-friipay-13hm",
    "location": "XRPL Developers Discord",
    "date": "February 15, 2023",
    "image": "AMAs.png",
    "end_date": "February 15, 2023"
    },
    { "name": "AMAs: On-chain Data with Bithomp",      
    "description": "A discuss with Bithomp about data infrastructure and their NFT integrations in one of the most popular explorers on the XRP Ledger.",
    "type": "ama",
    "link": "https://dev.to/ripplexdev/xrpl-developer-ama-bithomp-4a8d",
    "location": "XRPL Developers Discord",
    "date": "March 15, 2023",
    "image": "AMAs.png",
    "end_date": "March 15, 2023"
    },
    {
    "name": "XRPL Community Meetup: Madrid",      
    "description": "Get together with other Madrid-based members of the XRP Ledger community to network and discuss all things XRPL.",
    "type": "meetup",
    "link": "https://www.meetup.com/xrp-ledger-espana-madrid-y-barcelona/events/292597878",
    "location": "Madrid",
    "date": "April 29, 2023",
    "image": "Madrid.png",
    "end_date": "April 29, 2023" 
    },
    {
    "name": "APEX 2023: The XRPL Developer Summit",      
    "description": "Apex XRPL Developer Summit is the annual event where developers, contributors, and thought leaders come together to learn, build, share, network, and celebrate all things XRP Ledger.",
    "type": "conference",
    "link": "http://apexdevsummit.com",
    "location": "Amsterdam",
    "date": "September 6 - 8, 2023",
    "image": "Conference.png",
    "end_date": "September 8, 2023" 
    },
    { "name": "Community Calls #3",      
    "description": "An open chat with the XRP Ledger community about NFTs and the EVM sidechain testnet.",
    "type": "cc",
    "link": "https://discord.com/invite/xrpl",
    "location": "XRPL Developers Discord",
    "date": "March 30, 2023",
    "image": "CommunityCalls.png",
    "end_date": "March 30, 2023"
    },
    { "name": "XRPL Roundtable: XRPL @ Consensus",      
    "description": "A roundtable chat with those who represented the XRP Ledger at Consensus 2023.",
    "type": "ama",
    "link": "https://twitter.com/RippleXDev",
    "location": "Twitter Spaces",
    "date": "June 24, 2023",
    "image": "AMAs.png",
    "end_date": "June 24, 2023"
    },
    { "name": "XRPL BUIDLERS BOOTCAMP",      
    "description": "First XRPL Ideathon in Japan Held Ahead of Crypto Event IVS Crypto.",
    "type": "hackathon",
    "link": "https://lu.ma/xrpl_builders_bootcamp",
    "location": "Tokyo",
    "date": "June 25, 2023",
    "image": "Hackathons.png",
    "end_date": "June 25, 2023"
    },
    { "name": "XRPL Workshop at WebX Asia",      
    "description": "Workshop with XRP Ledger co-developer David Schwartz and leading Japanese XRPL developers.",
    "type": "conference",
    "link": "https://lu.ma/mn90h3h9",
    "location": "Tokyo",
    "date": "July 26, 2023",
    "image": "Conference.png",
    "end_date": "July 26, 2023"
    },
    { "name": "XRPL Summer Hackathon",      
    "description": "The XRPL Hackathon is all about supporting innovative projects and getting developers from diverse backgrounds to explore creative ideas and transition from centralized systems to the exciting world of blockchain. Bring your innovative projects to life and get a chance to secure up to $10,000 in funding.",
    "type": "hackathon",
    "link": "https://dorahacks.io/hackathon/xrpl-hackathon",
    "location": "Online",
    "date": "June 5, 2023 - July 30, 2023",
    "image": "Hackathons.png",
    "end_date": "July 30, 2023"
    },
    { "name": "AMAs: XRPL Developer AMAs",      
    "description": "A chat with Matt Mankins from Lorem Labs to discuss Kudos for Code and his recent XRPL Accelerator acceptance.",
    "type": "ama",
    "link": "http://xrpldevs.org/",
    "location": "XRPL Developers Discord",
    "date": "July 18, 2023",
    "image": "AMAs.png",
    "end_date": "July 18, 2023"
    },
    { "name": "Q3 2023 Ripple XRP Meetup",      
    "description": "Join your fellow Ripple XRP Enthusiasts for a 90-minute discussion. Topics: XRP, Flare, XRPL, Ripple (Company), General Crypto QA.",
    "type": "meetup",
    "link": "https://www.meetup.com/ripple-xrp-community/events/292740612",
    "location": "Online",
    "date": "July 13, 2023",
    "image": "Virtual-Event.png",
    "end_date": "July 13, 2023"
    },
    { "name": "XRPL Toronto Meetup",      
    "description": "Prepare for an evening of XRPL Toronto Meetup – a celebration of discovery and connection. Join enthusiasts, innovators, and developers for inspiring talks, conversations, and learning. All are welcome, from seasoned developers to curious newcomers.",
    "type": "meetup",
    "link": "https://www.meetup.com/xrpl-toronto-community-meetup/events/294766059",
    "location": "Downtown Toronto",
    "date": "August 14, 2023",
    "image": "event-meetup-toronto@2x.jpg",
    "end_date": "August 14, 2023"
    },
    { "name": "XRPL London Meetup (Accelerator Edition)",      
    "description": "Join us for a Happy Hour hosted by the XRPL Accelerator Team! Connect with fellow start-ups in the blockchain space and gain insights into cutting-edge projects and founders.",
    "type": "meetup",
    "link": "https://lu.ma/xrplacceleratorhappyhour",
    "location": "Central London",
    "date": "September 04, 2023",
    "image": "event-meetup-london.png",
    "end_date": "September 04, 2023"
    },
    {
    "name": "XRPL Accelerator Demo Day",      
    "description": "​​Join us for our very first XRPL Accelerator Demo Day in London. Witness pitches from nine portfolio startups, engage in Q&A sessions, and network with founders and investors. ",
    "type": "conference",
    "link": "https://lu.ma/xrplaccelerator",
    "location": "Central London and Online",
    "date": "September 05, 2023",
    "image": "Conference.png",
    "end_date": "September 05, 2023" 
    },
    { "name": "XRPL Hackathon - Apex 2023",      
    "description": "Join the XRPL Hackathon - APEX 2023, a week before the XRP Ledger's annual developer conference. Explore the Future of Finance and Web3 tracks, collaborate, learn, and compete for 10K USD in prizes.",
    "type": "hackathon",
    "link": "https://lu.ma/4h3bqfw1",
    "location": "Delft, Netherlands ",
    "date": "August 30, 2023 - August 31, 2023",
    "image": "Hackathons.png",
    "end_date": "August 31, 2023"
    },
    { "name": "XRPL Grants Info Session: Financial Inclusion Focused",      
    "description": "Join us for a live information session and Q&A on applying to XRPL Grants Wave 7. This session will provide a general overview of the XRPL Grants application for Wave 7, with a focus on Financial Inclusion projects.",
    "type": "info-session",
    "link": "https://www.youtube.com/watch?v=TgLaAXTZY7Q",
    "location": "Virtual - Zoom",
    "date": "September 05, 2023",
    "image": "InfoSessions.png",
    "end_date": "September 05, 2023"
    },
    { "name": "XRPL South Korea Meetup - XCCESS",      
    "description": "We are excited to introduce the XRP Ledger XCCESS - an exclusive meetup bringing together the brightest minds, innovators, and enthusiasts from South Korea's blockchain industry. Join us for an engaging experience during the Korea Blockchain Week.",
    "type": "meetup",
    "link": "https://lu.ma/xrplxccess",
    "location": "South Korea - JBK Tower",
    "date": "September 06, 2023",
    "image": "SouthKoreaMeetup.png",
    "end_date": "September 06, 2023"
    },
    { "name": "XRPL Grants Info Session: Decentralized Exchange (DEX) Focused",      
    "description": "Watch the recorded information session and Q&A on applying to XRPL Grants Wave 7. This session will provide a general overview of the XRPL Grants application for Wave 7, with a focus on Decentralized Exchange (DEX) projects.",
    "type": "info-session",
    "link": "https://www.youtube.com/watch?v=BbGu0QC5WEE",
    "location": "Virtual - Zoom",
    "date": "September 06, 2023",
    "image": "InfoSessions.png",
    "end_date": "September 06, 2023"
    },
    { "name": "XRPL Developers Discord AMA: Edge Wallet",      
    "description": "Join us for a live chat on Discord and learn more about Edge Wallet and how they are building on the XRP Ledger.",
    "type": "ama",
    "link": "http://xrpldevs.org/",
    "location": "XRPL Developers Discord",
    "date": "October 13, 2023",
    "image": "AMAs.png",
    "end_date": "October 13, 2023"
    },
    
    { "name": "XRPL Developers Reddit AMA: Real World Assets",      
    "description": "Join us for a live chat on Reddit and learn more about how developers are building real world assets with confidence on the XRP Ledger.",
    "type": "ama",
    "link": "https://xrplresources.org/rwa-ama?utm_source=web&utm_medium=web&utm_campaign=bwc",
    "location": "Virtual - Reddit",
    "date": "October 17, 2023",
    "image": "AMAs.png",
    "end_date": "October 17, 2023"
    },
    { "name": "XRPL Accelerator Demo Day",      
    "description": "Join us for XRPL Accelerator Demo Day in Singapore! Explore pitches from 11 promising startups building on the XRP Ledger, network with founders and investors, and kickstart the Singapore FinTech Festival. Webinar link coming soon!",
    "type": "meetup",
    "link": "https://www.eventbrite.co.uk/e/xrpl-demo-day-tickets-740650023157?aff=oddtdtcreator",
    "location": "Hybrid Singapore/Virtual Webinar",
    "date": "November 14, 2023",
    "image": "SouthKoreaMeetup.png",
    "end_date": "November 14, 2023"
    },
    { "name": "XRPL Blockhack Hackathon",      
    "description": "Join us at George Brown College's Waterfront Campus for workshops and talks on promoting growth for blockchain projects and ventures. We are supporting a for the most innovative application built on XRPL.",
    "type": "hackathon",
    "link": "https://blockhack-2023.devpost.com/",
    "location": "George Brown College - Waterfront Campus",
    "date": "October 20, 2023 - October 22, 2023",
    "image": "Hackathons.png",
    "end_date": "October 22, 2023"
    },
    
    { "name": "New Horizon: Innovate Without Limits: New Horizons Await",      
    "description": "Join us to kickstart the ecosystem of the upcoming EVM-compatible chain, opening new possibilities for developers to explore the limitless potential of our platform.",
    "type": "hackathon",
    "link": "https://newhorizon.devpost.com/",
    "location": "Virtual",
    "date": "October 19, 2023 - December 22, 2023",
    "image": "Hackathons.png",
    "end_date": "December 22, 2023"
    },
]
def categorize_dates():
    past = []
    upcoming = []
    today = datetime.today()
    for obj in events:
        end_date = datetime.strptime(obj['end_date'], '%B %d, %Y')
        if end_date < today:
            obj['type'] = obj['type'] + '-past'
            past.append(obj)
        else:
            obj['type'] = obj['type'] + '-upcoming'
            upcoming.append(obj)
    return {'past': past, 'upcoming': upcoming, 'all' : all}

export = {
    "categorize_dates": categorize_dates,
}
