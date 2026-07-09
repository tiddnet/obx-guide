#!/usr/bin/env python3
"""One-off generator for guide.obx.deals — ADR 0215."""
from pathlib import Path

OUT = Path("/Users/loaner/git/obx-guide")

ACCENT = "#2461a8"

NAV_TOWNS = [
    ("corolla", "Corolla"), ("duck", "Duck"), ("southern-shores", "Southern Shores"),
    ("kitty-hawk", "Kitty Hawk"), ("carova", "Carova"),
    ("kill-devil-hills", "Kill Devil Hills"), ("nags-head", "Nags Head"), ("south-nags-head", "South Nags Head"),
    ("rodanthe", "Rodanthe"), ("waves", "Waves"), ("salvo", "Salvo"), ("avon", "Avon"),
    ("buxton", "Buxton"), ("frisco", "Frisco"), ("hatteras-village", "Hatteras Village"),
    ("manteo", "Manteo"), ("ocracoke", "Ocracoke"),
]

REGIONS = [
    ("Northern OBX", ["corolla", "duck", "southern-shores", "kitty-hawk", "carova"]),
    ("Central OBX", ["kill-devil-hills", "nags-head", "south-nags-head"]),
    ("Hatteras Island", ["rodanthe", "waves", "salvo", "avon", "buxton", "frisco", "hatteras-village"]),
    ("Roanoke Island & Ocracoke", ["manteo", "ocracoke"]),
]

CSS = """  <style>
    :root {
      --ink: #17242e; --muted: #55697a; --rule: #d8e3ea;
      --accent: %ACCENT%; --accent-dark: #184a78; --bg: #f4f8fb; --card-bg: #fff;
      --nav-bg: #1A2B3C; --nav-text: #b8d0cc; --nav-active: #ffffff; --nav-gold: #E8B84B;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      background: var(--bg); color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-size: 17px; line-height: 1.6;
    }
    a { color: var(--accent-dark); }
    .site-nav { background: var(--nav-bg); position: sticky; top: 0; z-index: 100; border-bottom: 2px solid var(--nav-gold); }
    .site-nav-inner { max-width: 1000px; margin: 0 auto; padding: 0.6rem 1.25rem; }
    .nav-top-row { display: flex; align-items: center; }
    .nav-brand-obx, .nav-brand-suffix { font-weight: 800; font-size: 1.1rem; text-decoration: none; padding: 0.15rem 0; white-space: nowrap; }
    .nav-brand-obx { color: var(--nav-gold); margin-right: 0.45rem; }
    .nav-brand-obx:hover { color: var(--nav-active); }
    .nav-brand-suffix { color: var(--nav-active); margin-right: 0.75rem; }
    .nav-brand-suffix:hover { color: var(--nav-gold); }
    .nav-links { display: flex; flex-wrap: wrap; gap: 0.15rem 0; }
    .nav-links a { color: var(--nav-text); text-decoration: none; font-size: 0.83rem; font-weight: 500; padding: 0.3rem 0.6rem; white-space: nowrap; border-radius: 4px; }
    .nav-links a:hover { color: var(--nav-active); background: rgba(255,255,255,.08); }
    .nav-links a.current { color: var(--nav-active); background: rgba(232,184,74,.18); font-weight: 700; }
    .nav-cta { margin-left: auto; flex-shrink: 0; }
    .nav-cta a { display: inline-block; background: var(--nav-gold); color: #1A2B3C; font-weight: 700; padding: 0.4rem 0.85rem; border-radius: 5px; text-decoration: none; font-size: 0.82rem; margin: 0.6rem 0; }
    .page-hero { background: linear-gradient(160deg, #0d2540 0%, #184a78 55%, #2461a8 130%); color: #eaf3ff; padding: 2.8rem 1.5rem 2.4rem; }
    .page-hero-inner { max-width: 760px; margin: 0 auto; }
    .breadcrumb { font-size: 0.82rem; color: #a9cdf0; margin-bottom: 1rem; }
    .breadcrumb a { color: #cfe4fb; text-decoration: none; }
    .page-hero h1 { font-size: clamp(1.7rem, 3.6vw, 2.3rem); letter-spacing: -0.01em; line-height: 1.15; margin-bottom: 0.4rem; }
    .page-hero .tagline { font-size: 1.05rem; color: #cfe4fb; font-style: italic; }
    main { max-width: 760px; margin: 0 auto; padding: 2.6rem 1.5rem 5rem; }
    main p { margin-bottom: 1.1rem; font-size: 1.02rem; }
    .stat-bar {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
      border: 1px solid var(--rule); border-radius: 8px; overflow: hidden; margin: 0 0 1.8rem; background: #fff;
    }
    .stat-cell { padding: 0.9rem 0.7rem; text-align: center; border-right: 1px solid var(--rule); }
    .stat-cell:last-child { border-right: 0; }
    .stat-val { display: block; font-size: 1.15rem; font-weight: 700; color: var(--accent-dark); }
    .stat-lbl { display: block; font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.2rem; }
    .fit-box { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.8rem 0; }
    .fit-card { border-radius: 8px; padding: 1.1rem 1.3rem; font-size: 0.92rem; }
    .fit-card.best { background: #eef7f0; border-left: 3px solid #2a7a4b; }
    .fit-card.not { background: #fdf4ee; border-left: 3px solid #b5651d; }
    .fit-card h3 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
    .fit-card.best h3 { color: #2a7a4b; }
    .fit-card.not h3 { color: #b5651d; }
    .fit-card ul { padding-left: 1.1rem; }
    .fit-card li { margin-bottom: 0.3rem; }
    .access-note { background: #eef4fb; border-left: 3px solid var(--accent); border-radius: 8px; padding: 1.1rem 1.4rem; margin: 1.5rem 0; font-size: 0.93rem; }
    .access-note strong { color: var(--accent-dark); }
    .search-cta { text-align: center; padding: 1.6rem; margin-top: 2rem; background: var(--nav-bg); border-radius: 10px; }
    .search-cta p { color: var(--nav-text); margin-bottom: 0.9rem; font-size: 0.95rem; }
    .search-cta a.btn { display: inline-block; background: var(--nav-gold); color: #1A2B3C; font-weight: 700; padding: 0.6rem 1.4rem; border-radius: 6px; text-decoration: none; font-size: 0.9rem; }
    .region-block { margin-bottom: 2.6rem; }
    .region-title { font-size: 1.25rem; margin-bottom: 0.9rem; }
    .town-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.9rem; }
    .town-card { background: #fff; border: 1px solid var(--rule); border-radius: 8px; padding: 1rem 1.15rem; text-decoration: none; color: inherit; display: block; }
    .town-card:hover { box-shadow: 0 6px 16px rgba(36,97,168,.14); }
    .town-name { font-weight: 700; font-size: 1rem; margin-bottom: 0.2rem; }
    .town-tag { font-size: 0.82rem; color: var(--muted); font-style: italic; }
    footer { color: var(--muted); font-size: 0.87rem; margin-top: 3rem; border-top: 1px solid var(--rule); padding-top: 1.4rem; }
    footer a { text-decoration: none; }
    .hero-lede { max-width: 720px; margin: 0 auto; padding: 3rem 1.5rem 2.4rem; color: #eaf3ff; }
  </style>
""".replace("%ACCENT%", ACCENT)

GTAG = """  <script async src="https://www.googletagmanager.com/gtag/js?id=G-1P2LPD0VMY"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-1P2LPD0VMY');
  </script>
"""


def nav(active_slug):
    links = []
    for slug, label in NAV_TOWNS:
        cls = ' class="current"' if slug == active_slug else ""
        links.append(f'<a href="/{slug}/"{cls}>{label}</a>')
    return f"""  <nav class="site-nav" aria-label="OBX Deals network">
    <div class="site-nav-inner">
      <div class="nav-top-row">
        <a href="https://obx.deals/" class="nav-brand-obx">OBX</a><a href="/" class="nav-brand-suffix">Guide</a>
        <div class="nav-cta"><a href="https://search.obx.deals/">Search rentals &rarr;</a></div>
      </div>
      <div class="nav-links">
        {''.join(links)}
      </div>
    </div>
  </nav>
"""


TOWNS = {
    "corolla": dict(name="Corolla", region="Northern OBX",
        tagline="Big houses, wide beaches, and the road runs out here.",
        character="Corolla is where the Outer Banks goes big &mdash; the median rental here is six bedrooms, and multi-family groups treat it as the default. With 2,618 rental properties it's the largest vacation inventory on the northern beaches, most of it built in planned oceanside communities off Route 12. It's roughly 28 miles from Nags Head, which means you commit: you're not day-tripping to the central beaches on a whim.",
        best=["Large multi-family groups", "Big-house amenities (pools, game rooms)", "Lighthouse and wild-horse day trips", "People who want beach, not boardwalk"],
        not_ideal=["Couples or small groups", "Anyone who wants to be central to the whole OBX"],
        access="The paved road ends at the north end of Corolla &mdash; everything beyond (Carova) is 4WD beach driving only. The Currituck Beach Lighthouse is here and climbable in season.",
        n=2618, dist=28.3, beds="4&ndash;7 BR (median 6)", rate="$1,902&ndash;$5,152/wk"),
    "duck": dict(name="Duck", region="Northern OBX",
        tagline="The one OBX town you can actually walk.",
        character="Duck is the exception to the drive-everywhere rule: an incorporated town with a genuine center &mdash; shops and restaurants strung along a soundside boardwalk &mdash; where a family can park the car for a week and mostly leave it. The 1,356 rentals skew 4&ndash;6 bedrooms with a more boutique character than its neighbors. It's about 18 miles from Nags Head, close enough for day trips south.",
        best=["Families wanting walkability", "Food and shopping without driving", "A more polished, low-key vibe", "Soundside sunsets"],
        not_ideal=["Budget-conscious groups", "Anyone wanting nightlife"],
        access="Duck's town center is genuinely walkable &mdash; a soundfront boardwalk connects shops and restaurants, which is rare on the Outer Banks.",
        n=1356, dist=18.1, beds="4&ndash;6 BR (median 5)", rate="$1,704&ndash;$4,465/wk"),
    "southern-shores": dict(name="Southern Shores", region="Northern OBX",
        tagline="The quiet one &mdash; residential by design, and it shows.",
        character="Southern Shores is an incorporated town that has deliberately stayed residential: less commercial development than Duck to the north or Kitty Hawk to the south, and it feels like a neighborhood that happens to rent houses rather than a resort. Inventory is smaller &mdash; 528 rentals, mostly 4&ndash;6 bedrooms &mdash; at 14 miles from Nags Head, well positioned between quiet at home and everything else a short drive away.",
        best=["Families wanting peace and quiet", "Repeat visitors who've outgrown the crowds", "Central location without the commercial strip"],
        not_ideal=["Groups wanting restaurants and shops in walking distance", "First-timers who want the “classic” busy beach-town scene"],
        access="Southern Shores sits at the foot of the Wright Memorial Bridge &mdash; it's the first town you reach coming onto the northern beaches, which makes changeover-day arrivals easier than the towns farther north.",
        n=528, dist=13.6, beds="4&ndash;6 BR (median 4)", rate="$1,865&ndash;$4,634/wk"),
    "kitty-hawk": dict(name="Kitty Hawk", region="Northern OBX",
        tagline="Central, practical, and the best value on the northern beaches.",
        character="Kitty Hawk is the working end of the northern OBX &mdash; smaller houses, lower prices, and a location that puts everything within easy reach: 10 miles from Nags Head, minutes from the bridge, groceries and errands on US-158. It's less resort-y than Duck or Corolla, and that's the point. Groups who care more about beach time than house theatrics tend to land here and come back.",
        best=["Value-focused families", "Smaller groups", "A central base for exploring the whole OBX", "Quick on/off-island access"],
        not_ideal=["Large groups needing 6+ bedrooms", "Anyone wanting an upscale resort feel"],
        access="The Wright brothers' first flight is named for Kitty Hawk because of the weather station that handled their telegrams &mdash; the actual flight site and memorial are just south in what's now Kill Devil Hills.",
        n=660, dist=9.6, beds="3&ndash;4 BR (median 4)", rate="$1,330&ndash;$2,822/wk"),
    "carova": dict(name="Carova", region="Northern OBX",
        tagline="No pavement, no shops, wild horses in the yard.",
        character="Carova isn't a town so much as a decision. There are no paved roads &mdash; you reach it by driving the beach north from where Route 12 ends in Corolla, 4WD required, tides consulted. The wild horses that made the area famous walk through yards and down the sand lanes. Its 241 rentals run 4&ndash;6 bedrooms, and every one of them requires you to haul groceries in over the sand. That's the price of genuine isolation, and the people who choose it consider it a bargain.",
        best=["Groups wanting true seclusion", "Wild-horse encounters", "People who find beach driving part of the fun", "Unplugging"],
        not_ideal=["Anyone without a 4WD vehicle", "Travelers who want restaurants or shops nearby", "First-time OBX visitors who want to explore widely"],
        access="4WD is required for all access &mdash; there is no paved road into Carova; you drive the beach north from the end of NC-12 in Corolla, and rental agreements assume it.",
        n=241, dist=40.1, beds="4&ndash;6 BR (median 5)", rate="$1,723&ndash;$4,870/wk"),
    "kill-devil-hills": dict(name="Kill Devil Hills", region="Central OBX",
        tagline="Where flight started, and where everything on the OBX is close.",
        character="Kill Devil Hills is the working center of the Outer Banks beach towns &mdash; 1,244 rentals, the densest commercial stretch on the beach road, and a grocery run that never takes more than ten minutes. Houses run 3&ndash;5 bedrooms, which makes it the practical pick for a family that wants the beach plus restaurants, shops, and errands within a bike ride. It's the town you choose when convenience outranks seclusion.",
        best=["First-time OBX visitors", "Families who want restaurants and groceries close", "Mid-size groups (3&ndash;5BR)", "Budget-conscious weeks near the action"],
        not_ideal=["Travelers wanting quiet or remote beaches", "Very large groups (few 6BR+ houses)"],
        access="The Wright Brothers National Memorial &mdash; site of the first powered flight in 1903 &mdash; sits in the middle of town, and the monument hill is visible from much of the bypass.",
        n=1244, dist=5.8, beds="3&ndash;5 BR (median 3)", rate="$1,239&ndash;$2,855/wk"),
    "nags-head": dict(name="Nags Head", region="Central OBX",
        tagline="The classic OBX beach town, from old cottages to big group houses.",
        character="Nags Head is the reference point the rest of the central OBX gets measured against &mdash; 1,310 rentals, the largest inventory in this guide, spanning weathered historic beach cottages to 8-bedroom group houses. That range is the point: it's the one central town where a couple's cottage week and a three-family reunion both fit. Jockey's Ridge anchors the sound side; the beach road carries the old-OBX look the postcards are based on.",
        best=["Large group and multi-family stays", "Travelers who want the traditional OBX feel", "Widest choice of house sizes", "Jockey's Ridge sunsets, hang gliding, and sandboarding"],
        not_ideal=["Anyone wanting a uniform, newer-build neighborhood", "The lowest rates in the central OBX"],
        access="Jockey's Ridge State Park protects the tallest natural sand dune system on the East Coast, and it's free to enter and climb.",
        n=1310, dist=0.0, beds="3&ndash;8 BR (median 5)", rate="$1,414&ndash;$4,004/wk"),
    "south-nags-head": dict(name="South Nags Head", region="Central OBX",
        tagline="Nags Head's quiet end &mdash; beach houses, few storefronts, open road south.",
        character="South Nags Head is what happens when the beach road keeps going but the commercial development stops. It's a narrow, residential strip of 517 rentals about three miles from Nags Head proper &mdash; close enough that dinner and groceries are a short drive, far enough that evenings are just houses, dunes, and ocean. People who book here tend to rebook here: it trades convenience for a beach that feels like yours.",
        best=["Quiet, residential beach weeks", "Repeat visitors who know what they want", "Couples and smaller families", "Anglers heading to Oregon Inlet"],
        not_ideal=["Walk-to-restaurants trips", "Nightlife seekers"],
        access="South Nags Head ends at Oregon Inlet, the crossing point to Hatteras Island &mdash; day trips down Hatteras start closer here than from anywhere else in the central OBX.",
        n=517, dist=2.7, beds="3&ndash;5 BR (median 4)", rate="$1,295&ndash;$2,795/wk"),
    "rodanthe": dict(name="Rodanthe", region="Hatteras Island",
        tagline="First stop past the bridge, and it feels like it.",
        character="Cross the Marc Basnight Bridge from Nags Head, drive about 27 miles of NC-12, and Rodanthe is the first village you reach &mdash; the northern edge of the tri-villages. It's noticeably quieter and less built-up than the towns north of Oregon Inlet, with a real surf-and-fishing streak underneath the rental inventory. Good for people who want Hatteras Island proper without driving to the bottom of it.",
        best=["Surf-focused trips", "Fishing weeks", "Couples and mid-size families", "Travelers who want quiet over amenities"],
        not_ideal=["Nightlife seekers", "Anyone wanting shops and restaurants within walking distance"],
        access="The Marc Basnight Bridge over Oregon Inlet is the only road onto Hatteras Island &mdash; every drive down starts with that crossing.",
        n=399, dist=26.9, beds="2&ndash;5 BR (median 4)", rate="$1,015&ndash;$2,552/wk"),
    "waves": dict(name="Waves", region="Hatteras Island",
        tagline="The tri-villages' quiet middle, with wind on the sound side.",
        character="Waves sits between Rodanthe and Salvo, about 21 miles down NC-12, and blends into both &mdash; the tri-villages read as one continuous strip. What sets it apart is the sound side: this stretch is a genuine kiteboarding and windsurfing zone, with shallow water and steady wind drawing riders all season. Houses skew bigger here, with weekly rates typically gentler than the northern beaches.",
        best=["Kiteboarders and windsurfers", "Larger family groups", "Multi-family trips", "Quiet beach weeks"],
        not_ideal=["Walkable-town seekers", "Travelers who want a commercial strip"],
        access="Waves has no hard boundary with its neighbors &mdash; you'll pass through Rodanthe on NC-12 to get here, and Salvo starts before you notice Waves ended.",
        n=397, dist=21.0, beds="4&ndash;7 BR (median 5)", rate="$1,036&ndash;$2,800/wk"),
    "salvo": dict(name="Salvo", region="Hatteras Island",
        tagline="Southernmost, smallest, and quietest of the tri-villages.",
        character="Salvo is where the tri-village strip ends and the long undeveloped run of Cape Hatteras National Seashore toward Avon begins. It's the smallest of the three &mdash; about 216 rental properties &mdash; with minimal commercial development, which is either the drawback or the entire point depending on who's asking. Pick Salvo if you're planning to cook at the house, walk to the beach, and not go anywhere.",
        best=["Total quiet", "Families who self-cater", "Beach-and-book vacations", "Off-the-grid feel with paved-road access"],
        not_ideal=["Anyone who wants restaurants nearby", "First-timers wanting the full OBX amenity set"],
        access="South of Salvo, NC-12 runs through miles of national seashore with no development until Avon &mdash; the emptiest stretch of road on the island.",
        n=216, dist=26.7, beds="3&ndash;6 BR (median 4)", rate="$1,050&ndash;$2,555/wk"),
    "avon": dict(name="Avon", region="Hatteras Island",
        tagline="Hatteras Island's practical home base.",
        character="Avon is the island's supply hub &mdash; the town with a proper grocery store, restaurants, and surf shops, roughly 42 miles from Nags Head. That makes it the default base for a week on Hatteras: close enough to Buxton's lighthouse and surf, stocked enough that you're not driving an hour for provisions. It's also home to Island Creek, a soundfront neighborhood well known in the wind-sports crowd.",
        best=["First Hatteras trips", "Families wanting amenities", "Longer stays", "A central base for exploring the whole island"],
        not_ideal=["Travelers wanting the remotest possible feel", "Big-group houses (inventory skews mid-size)"],
        access="Avon has the only full-size grocery store on this stretch of the island &mdash; a real logistical advantage over the tri-villages to the north.",
        n=576, dist=42.0, beds="3&ndash;5 BR (median 4)", rate="$917&ndash;$2,240/wk"),
    "buxton": dict(name="Buxton", region="Hatteras Island",
        tagline="The lighthouse, the point, and the best-known surf on the island.",
        character="Buxton sits at the elbow of Hatteras Island, about 48 miles down, and it's the village with the landmarks: the Cape Hatteras Lighthouse &mdash; the tallest brick lighthouse in the US &mdash; and the Haulover Day Use Area, better known as Canadian Hole, a nationally known kiteboarding and windsurfing spot on the sound. The ocean side carries a serious surfing reputation. Housing runs smaller than most OBX towns &mdash; built for couples and small crews chasing water, not compounds.",
        best=["Surfers", "Kiteboarders and windsurfers", "Couples", "Lighthouse and seashore sightseeing", "Budget-conscious water people"],
        not_ideal=["Large groups needing big houses", "Luxury-amenity hunters"],
        access="The Cape Hatteras Lighthouse is in Buxton, inside Cape Hatteras National Seashore &mdash; the island's most-visited landmark.",
        n=303, dist=47.5, beds="1&ndash;3 BR (median 2)", rate="$910&ndash;$1,944/wk"),
    "frisco": dict(name="Frisco", region="Hatteras Island",
        tagline="Buxton's quieter neighbor, one village further down.",
        character="Frisco sits just south of Buxton, about 49 miles from Nags Head, and trades Buxton's landmark traffic for calm. You're minutes from Canadian Hole and the lighthouse without staying in the middle of that scene. It's also home to the Frisco Native American Museum. A good pick for people who want Buxton's water access with fewer people around.",
        best=["Quiet stays near Buxton's attractions", "Small families", "Value seekers", "Museum and seashore days"],
        not_ideal=["Big groups", "Anyone wanting restaurants and shops at hand"],
        access="Frisco puts you within a few miles of both Canadian Hole and the Cape Hatteras Lighthouse &mdash; close to the action without being in it.",
        n=260, dist=48.8, beds="3&ndash;4 BR (median 3)", rate="$857&ndash;$2,100/wk"),
    "hatteras-village": dict(name="Hatteras Village", region="Hatteras Island",
        tagline="The end of the road &mdash; literally.",
        character="NC-12 ends here. Hatteras Village is the southernmost settlement on the island, about 42 miles from Nags Head, and keeps a working-waterfront character: charter boats, fishing culture, and a local feel that the northern beaches lost decades ago. It's also the largest rental market on the island, and the jumping-off point for Ocracoke.",
        best=["Fishing and charter trips", "Ocracoke day trips", "Remote-feel seekers", "Groups wanting range in house size and price"],
        not_ideal=["Travelers who want to be central on the island", "Short first-timer trips"],
        access="The free NC-operated Hatteras&ndash;Ocracoke ferry departs from the village &mdash; roughly a 45&ndash;60 minute crossing, no reservation needed, on a seasonal schedule.",
        n=868, dist=41.7, beds="3&ndash;6 BR (median 4)", rate="$895&ndash;$2,995/wk"),
    "manteo": dict(name="Manteo", region="Roanoke Island & Ocracoke",
        tagline="The Outer Banks town that isn't on the banks.",
        character="Manteo sits on Roanoke Island, the piece of land tucked between the barrier islands and the mainland &mdash; you reach it via US-64, not the beach road. This is a historic waterfront town with a walkable downtown built around its harbor, not a row of beach houses behind a dune. It's also where the Outer Banks' oldest story lives: Roanoke Island is the site of the 16th-century English colony that vanished, the Lost Colony.",
        best=["Couples and small families who want a real town", "A downtown you can walk, a harbor, history within reach", "Shoulder-season travelers", "Anyone who's done the beach-house week and wants a different shape of trip"],
        not_ideal=["Groups who want to walk to the ocean &mdash; there's no ocean beach in Manteo itself", "Large groups needing 6+ bedrooms (thin inventory)"],
        access="Reached via US-64 across the Virginia Dare Memorial Bridge &mdash; a separate approach from the NC-12 beach corridor. Nags Head is roughly a 10-minute drive east.",
        n=184, dist=3.4, beds="1&ndash;4 BR (median 3)", rate="$1,809&ndash;$2,939/wk"),
    "ocracoke": dict(name="Ocracoke", region="Roanoke Island & Ocracoke",
        tagline="The island you can only reach by boat.",
        character="No bridge, no road. Ocracoke connects to the rest of the world by ferry, and that single fact is the whole character of the place. The village sits at the island's south end around a working harbor, with the Ocracoke Lighthouse nearby &mdash; one of the oldest operating lighthouses on the East Coast. Because getting here takes commitment, the crowds thin out and the pace drops.",
        best=["People who want the trip itself to be the point", "A real island, a walkable village, beaches with room to spread out", "Return visitors who've outgrown the busier towns", "Value hunters"],
        not_ideal=["Anyone who hates logistics or wants to day-trip elsewhere on a whim", "Travelers who need to plan around a fixed schedule"],
        access="Free ferry from the south end of Hatteras Island (roughly 45&ndash;60 minutes), or longer toll ferries from Swan Quarter and Cedar Island on the mainland. Check schedules before you book your arrival day.",
        n=521, dist=56.4, beds="2&ndash;4 BR (median 3)", rate="$1,303&ndash;$2,330/wk"),
}

SLUG_TO_COMMUNITY = {
    "corolla": "corolla", "duck": "duck", "southern-shores": "southern_shores",
    "kitty-hawk": "kitty_hawk", "carova": "carova",
    "kill-devil-hills": "kill_devil_hills", "nags-head": "nags_head", "south-nags-head": "south_nags_head",
    "rodanthe": "rodanthe", "waves": "waves", "salvo": "salvo", "avon": "avon",
    "buxton": "buxton", "frisco": "frisco", "hatteras-village": "hatteras_village",
    "manteo": "manteo", "ocracoke": "ocracoke",
}

# ADR 0216 — real town centroids (avg of scraped property coordinates),
# used for Place schema JSON-LD. Tier 1/2 public data only.
COORDS = {
    "corolla": (36.3279, -75.81135), "duck": (36.18639, -75.75606),
    "southern-shores": (36.12465, -75.72938), "kitty-hawk": (36.07312, -75.6996),
    "carova": (36.49675, -75.85825), "kill-devil-hills": (36.02257, -75.67066),
    "nags-head": (35.94883, -75.62126), "south-nags-head": (35.91162, -75.60552),
    "rodanthe": (35.57391, -75.49155), "waves": (35.65245, -75.53447),
    "salvo": (35.57887, -75.48589), "avon": (35.34761, -75.50627),
    "buxton": (35.26354, -75.55444), "frisco": (35.2425, -75.61862),
    "hatteras-village": (35.34577, -75.58423), "manteo": (35.91554, -75.66529),
    "ocracoke": (35.15998, -75.88039),
}


def _json_ld(slug, t):
    import json as _json
    lat, lng = COORDS[slug]
    place = {
        "@context": "https://schema.org",
        "@type": "Place",
        "name": t["name"],
        "description": t["tagline"],
        "address": {"@type": "PostalAddress", "addressLocality": t["name"],
                     "addressRegion": "NC", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
        "url": f"https://guide.obx.deals/{slug}/",
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "OBX Guide", "item": "https://guide.obx.deals/"},
            {"@type": "ListItem", "position": 2, "name": t["region"]},
            {"@type": "ListItem", "position": 3, "name": t["name"], "item": f"https://guide.obx.deals/{slug}/"},
        ],
    }
    return (f'  <script type="application/ld+json">{_json.dumps(place)}</script>\n'
            f'  <script type="application/ld+json">{_json.dumps(breadcrumb)}</script>\n')


def town_page(slug, t):
    best_li = "\n".join(f"          <li>{x}</li>" for x in t["best"])
    not_li = "\n".join(f"          <li>{x}</li>" for x in t["not_ideal"])
    search_url = f"https://search.obx.deals/?community={SLUG_TO_COMMUNITY[slug]}"
    json_ld = _json_ld(slug, t)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{GTAG}  <title>{t['name']} — OBX Area Guide</title>
  <meta name="description" content="{t['tagline']} {t['name']} vacation rental guide: what it's like, who it's for, real access facts.">
  <meta property="og:title" content="{t['name']} — OBX Area Guide">
  <meta property="og:description" content="{t['tagline']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://guide.obx.deals/{slug}/">
  <meta property="og:image" content="https://obx.deals/images/hero.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['name']} — OBX Area Guide">
  <meta name="twitter:description" content="{t['tagline']}">
  <meta name="twitter:image" content="https://obx.deals/images/hero.png">
  <link rel="canonical" href="https://guide.obx.deals/{slug}/">
  <link rel="icon" href="https://obx.deals/favicon.ico">
{json_ld}{CSS}</head>
<body>
{nav(slug)}
  <div class="page-hero">
    <div class="page-hero-inner">
      <nav class="breadcrumb"><a href="/">OBX Guide</a> &middot; {t['region']} &middot; {t['name']}</nav>
      <h1>{t['name']}</h1>
      <p class="tagline">{t['tagline']}</p>
    </div>
  </div>
  <main>
    <div class="stat-bar">
      <div class="stat-cell"><span class="stat-val">{t['n']:,}</span><span class="stat-lbl">Rentals</span></div>
      <div class="stat-cell"><span class="stat-val">{t['dist']:.0f} mi</span><span class="stat-lbl">From Nags Head</span></div>
      <div class="stat-cell"><span class="stat-val">{t['beds']}</span><span class="stat-lbl">Typical size</span></div>
      <div class="stat-cell"><span class="stat-val">{t['rate']}</span><span class="stat-lbl">Typical rate (25&ndash;75th pct)</span></div>
    </div>

    <p>{t['character']}</p>

    <div class="fit-box">
      <div class="fit-card best">
        <h3>Best for</h3>
        <ul>
{best_li}
        </ul>
      </div>
      <div class="fit-card not">
        <h3>Not ideal for</h3>
        <ul>
{not_li}
        </ul>
      </div>
    </div>

    <div class="access-note"><strong>Access &amp; character note:</strong> {t['access']}</div>

    <div class="search-cta">
      <p>See what's actually available in {t['name']} right now.</p>
      <a class="btn" href="{search_url}">Search {t['name']} rentals &rarr;</a>
    </div>

    <footer>
      <a href="https://obx.deals/">obx.deals</a> &middot;
      <a href="https://search.obx.deals/">Search all rentals</a> &middot;
      <a href="/">All OBX towns</a>
    </footer>
  </main>
</body>
</html>
"""


def index_page():
    region_blocks = []
    for region, slugs in REGIONS:
        cards = []
        for slug in slugs:
            t = TOWNS[slug]
            cards.append(f"""    <a class="town-card" href="/{slug}/">
      <div class="town-name">{t['name']}</div>
      <div class="town-tag">{t['tagline']}</div>
    </a>""")
        region_blocks.append(f"""  <div class="region-block">
    <h2 class="region-title">{region}</h2>
    <div class="town-grid">
{chr(10).join(cards)}
    </div>
  </div>""")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{GTAG}  <title>OBX Area Guide — Which Outer Banks Town Is Right for You?</title>
  <meta name="description" content="A real, data-backed guide to all 17 Outer Banks towns — who each one is for, typical rental sizes and prices, real access facts (4WD, ferries, bridges).">
  <meta property="og:title" content="OBX Area Guide">
  <meta property="og:description" content="Which Outer Banks town is right for your trip? 17 towns, real data, no fluff.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://guide.obx.deals/">
  <meta property="og:image" content="https://obx.deals/images/hero.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="OBX Area Guide">
  <meta name="twitter:description" content="Which Outer Banks town is right for your trip? 17 towns, real data, no fluff.">
  <meta name="twitter:image" content="https://obx.deals/images/hero.png">
  <link rel="canonical" href="https://guide.obx.deals/">
  <link rel="icon" href="https://obx.deals/favicon.ico">
{CSS}</head>
<body>
{nav("")}
  <div class="hero-lede" style="background:linear-gradient(160deg, #0d2540 0%, #184a78 55%, #2461a8 130%);">
    <h1 style="font-size:clamp(1.9rem,4vw,2.5rem);letter-spacing:-0.01em;margin-bottom:1rem;">Which Outer Banks town is actually right for you?</h1>
    <p style="font-size:1.05rem;margin-bottom:0.9rem;">The Outer Banks isn't one place. It's a 100-mile string of towns and villages that vary more than the postcards suggest — Corolla's big-house resort feel has almost nothing in common with Ocracoke's ferry-only isolation or Manteo's walkable historic downtown, and picking the wrong one for your trip is the single easiest way to end up disappointed with an otherwise good vacation.</p>
    <p style="font-size:1.05rem;">This guide covers all 17 towns, grounded in real data from the properties we track — typical rental sizes, typical prices, and the access facts that actually matter (does it need 4WD, is there a ferry, how far is it really).</p>
  </div>
  <main>
{chr(10).join(region_blocks)}
    <footer>
      <a href="https://obx.deals/">obx.deals</a> &middot;
      <a href="https://search.obx.deals/">Search all rentals</a> &middot;
      <a href="https://windsports.obx.deals/">Wind sports guide</a>
    </footer>
  </main>
</body>
</html>
"""


for slug, t in TOWNS.items():
    (OUT / slug / "index.html").write_text(town_page(slug, t), encoding="utf-8")

(OUT / "index.html").write_text(index_page(), encoding="utf-8")

print(f"wrote {len(TOWNS)} town pages + index")
