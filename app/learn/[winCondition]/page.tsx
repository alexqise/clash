import Link from "next/link"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { ChevronRight, Trophy, ArrowLeft, ArrowRight } from "lucide-react"
import { notFound } from "next/navigation"

interface WinConditionPageProps {
  params: {
    winCondition: string
  }
}

export default function WinConditionPage({ params }: WinConditionPageProps) {
  // This would normally come from a database or API
  const winConditions = {
    "hog-rider": {
      name: "Hog Rider",
      elixir: 4,
      description: "Fast building-targeting unit that deals significant damage.",
      strengths: [
        "Fast movement speed",
        "Targets buildings directly",
        "Moderate health for its cost",
        "Can jump over the river",
      ],
      weaknesses: ["Vulnerable to swarms", "Easily distracted by buildings", "No splash damage"],
      counters: [
        {
          name: "Cannon",
          elixir: 3,
          description: "Positive elixir trade. Place in the middle to pull the Hog Rider.",
        },
        {
          name: "Tornado",
          elixir: 3,
          description: "Can activate King Tower in 2v2 or pull to other lane.",
        },
        {
          name: "Tombstone",
          elixir: 3,
          description: "Distracts Hog and spawns skeletons when destroyed.",
        },
        {
          name: "Mini P.E.K.K.A",
          elixir: 4,
          description: "High damage dealer that can take out Hog in a few hits.",
        },
      ],
      tips: [
        "Place buildings 4 tiles from the river to maximize pull distance",
        "Time your counters just as the Hog crosses the bridge",
        "Use small troops to surround the Hog if you don't have buildings",
        "Consider using Tornado to activate your King Tower early in the match",
      ],
    },
    golem: {
      name: "Golem",
      elixir: 8,
      description: "High health tank that explodes into two Golemites upon death.",
      strengths: ["Extremely high health", "Death damage", "Splits into Golemites", "Great tank for support troops"],
      weaknesses: [
        "Very expensive at 8 elixir",
        "Slow movement speed",
        "Vulnerable to Inferno Tower/Dragon",
        "Weak against heavy pushes in opposite lane",
      ],
      counters: [
        {
          name: "Inferno Tower",
          elixir: 5,
          description: "Melts the Golem with increasing damage over time.",
        },
        {
          name: "Inferno Dragon",
          elixir: 4,
          description: "Mobile counter that can transition into a counterpush.",
        },
        {
          name: "P.E.K.K.A",
          elixir: 7,
          description: "High damage dealer that can counter Golem and support troops.",
        },
        {
          name: "Opposite Lane Pressure",
          elixir: "Varies",
          description: "Force opponent to spend elixir defending instead of supporting Golem.",
        },
      ],
      tips: [
        "Push the opposite lane immediately when they place Golem in the back",
        "Save your Inferno Tower/Dragon for the Golem, not support troops",
        "Use small troops to distract support units behind the Golem",
        "Position buildings centrally to maximize pull distance",
      ],
    },
    // Add more win conditions as needed
  }

  const condition = winConditions[params.winCondition]

  if (!condition) {
    notFound()
  }

  // Find next and previous win condition for navigation
  const conditionKeys = Object.keys(winConditions)
  const currentIndex = conditionKeys.indexOf(params.winCondition)
  const prevCondition = currentIndex > 0 ? conditionKeys[currentIndex - 1] : null
  const nextCondition = currentIndex < conditionKeys.length - 1 ? conditionKeys[currentIndex + 1] : null

  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-blue-900 text-white shadow-md">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Trophy className="h-8 w-8 text-yellow-400" />
            <h1 className="text-xl md:text-2xl font-bold">Clash Counter Academy</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link href="/" className="hover:text-yellow-400 font-medium">
              Home
            </Link>
            <Link href="/learn" className="hover:text-yellow-400 font-medium">
              Learn
            </Link>
            <Link href="/quiz" className="hover:text-yellow-400 font-medium">
              Quiz
            </Link>
            <Link href="/about" className="hover:text-yellow-400 font-medium">
              About
            </Link>
          </nav>
          <Button variant="outline" className="md:hidden bg-transparent border-white text-white hover:bg-blue-800">
            Menu
          </Button>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <div className="flex items-center gap-2 mb-6">
            <Link href="/" className="text-blue-600 hover:underline">
              Home
            </Link>
            <ChevronRight className="h-4 w-4" />
            <Link href="/learn" className="text-blue-600 hover:underline">
              Learn
            </Link>
            <ChevronRight className="h-4 w-4" />
            <span>{condition.name}</span>
          </div>

          <div className="bg-white rounded-lg shadow-md overflow-hidden mb-8">
            <div className="md:flex">
              <div className="md:w-1/3 bg-blue-100 p-6 flex items-center justify-center">
                <div className="text-center">
                  <div className="relative h-48 w-48 mx-auto mb-4">
                    <Image
                      src={`/placeholder.svg?height=192&width=192&text=${encodeURIComponent(condition.name)}`}
                      alt={condition.name}
                      fill
                      className="object-contain"
                    />
                  </div>
                  <h1 className="text-2xl font-bold">{condition.name}</h1>
                  <p className="text-blue-800">{condition.elixir} Elixir</p>
                </div>
              </div>
              <div className="md:w-2/3 p-6">
                <h2 className="text-xl font-bold mb-4">Overview</h2>
                <p className="mb-4">{condition.description}</p>

                <div className="grid md:grid-cols-2 gap-6">
                  <div>
                    <h3 className="font-bold text-green-700 mb-2">Strengths</h3>
                    <ul className="list-disc pl-5 space-y-1">
                      {condition.strengths.map((strength, index) => (
                        <li key={index}>{strength}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <h3 className="font-bold text-red-700 mb-2">Weaknesses</h3>
                    <ul className="list-disc pl-5 space-y-1">
                      {condition.weaknesses.map((weakness, index) => (
                        <li key={index}>{weakness}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <h2 className="text-2xl font-bold mb-4">Best Counters</h2>
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            {condition.counters.map((counter, index) => (
              <Card key={index} className="flex">
                <div className="w-1/4 bg-blue-50 flex items-center justify-center p-4">
                  <div className="text-center">
                    <div className="relative h-16 w-16 mx-auto">
                      <Image
                        src={`/placeholder.svg?height=64&width=64&text=${encodeURIComponent(counter.name)}`}
                        alt={counter.name}
                        fill
                        className="object-contain"
                      />
                    </div>
                    <p className="text-sm font-medium mt-2">{counter.name}</p>
                    <p className="text-xs text-blue-800">{counter.elixir} Elixir</p>
                  </div>
                </div>
                <CardContent className="w-3/4 p-4">
                  <p>{counter.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>

          <h2 className="text-2xl font-bold mb-4">Pro Tips</h2>
          <div className="bg-white rounded-lg shadow-md p-6 mb-8">
            <ul className="space-y-3">
              {condition.tips.map((tip, index) => (
                <li key={index} className="flex items-start">
                  <span className="inline-flex items-center justify-center rounded-full bg-blue-100 text-blue-800 h-6 w-6 text-sm font-medium mr-3 mt-0.5">
                    {index + 1}
                  </span>
                  <span>{tip}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="flex justify-between mt-8">
            {prevCondition ? (
              <Button asChild variant="outline">
                <Link href={`/learn/${prevCondition}`}>
                  <ArrowLeft className="mr-2 h-4 w-4" />
                  Previous: {winConditions[prevCondition].name}
                </Link>
              </Button>
            ) : (
              <div></div>
            )}

            {nextCondition ? (
              <Button asChild variant="outline">
                <Link href={`/learn/${nextCondition}`}>
                  Next: {winConditions[nextCondition].name}
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
              </Button>
            ) : (
              <div></div>
            )}
          </div>

          <div className="text-center mt-12">
            <Button asChild className="bg-blue-600 hover:bg-blue-700">
              <Link href={`/quiz/${params.winCondition}`}>Test Your Knowledge</Link>
            </Button>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center gap-2 mb-4 md:mb-0">
              <Trophy className="h-6 w-6 text-yellow-400" />
              <span className="text-lg font-bold">Clash Counter Academy</span>
            </div>
            <div className="flex gap-6">
              <Link href="/" className="hover:text-yellow-400">
                Home
              </Link>
              <Link href="/learn" className="hover:text-yellow-400">
                Learn
              </Link>
              <Link href="/quiz" className="hover:text-yellow-400">
                Quiz
              </Link>
              <Link href="/about" className="hover:text-yellow-400">
                About
              </Link>
            </div>
          </div>
          <div className="mt-6 text-center md:text-left text-gray-400 text-sm">
            <p>© {new Date().getFullYear()} Clash Counter Academy. Not affiliated with Supercell.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
